// SocialBrand site JS: theme, nav, reveal, counters. No dependencies.
(function () {
  var root = document.documentElement;
  var tbtn = document.getElementById("themeToggle");
  if (tbtn) tbtn.addEventListener("click", function () {
    var dark = root.dataset.theme === "dark";
    if (dark) { delete root.dataset.theme; localStorage.setItem("sb-theme", "light"); }
    else { root.dataset.theme = "dark"; localStorage.setItem("sb-theme", "dark"); }
  });

  var burger = document.getElementById("burger"), nav = document.getElementById("nav");
  if (burger && nav) burger.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // reveal on scroll
  var els = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window && els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add("in"); });

  // animated counters: <span class="n" data-count="98" data-suffix="%">
  var counters = document.querySelectorAll("[data-count]");
  function animate(el) {
    var target = parseFloat(el.dataset.count), suffix = el.dataset.suffix || "", prefix = el.dataset.prefix || "";
    var dec = (el.dataset.count.split(".")[1] || "").length;
    var t0 = null, dur = 1400;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + (target * eased).toFixed(dec) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animate(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  // simple email gate for resources: reveals content after a lead form posts
  document.querySelectorAll("form[data-gate]").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var email = f.querySelector("input[type=email]").value;
      var data = new FormData(f);
      fetch(f.action, { method: "POST", body: data, headers: { Accept: "application/json" } }).catch(function () {});
      var gate = document.getElementById(f.dataset.gate);
      if (gate) { gate.hidden = false; gate.scrollIntoView({ behavior: "smooth" }); }
      f.hidden = true;
      var ok = document.getElementById(f.dataset.gate + "-ok");
      if (ok) ok.hidden = false;
    });
  });

  // ---- Command palette (Ctrl/Cmd+K) ----
  (function () {
    var overlay = document.getElementById("cmdk");
    var input = document.getElementById("cmdkInput");
    var list = document.getElementById("cmdkList");
    var empty = document.getElementById("cmdkEmpty");
    var openBtn = document.getElementById("cmdOpen");
    var pages = window.SB_PAGES || [];
    if (!overlay || !input || !list || !pages.length) return;

    var active = 0, results = [], lastFocus = null;

    function score(q, text) {
      if (!q) return 1;
      text = text.toLowerCase();
      var idx = text.indexOf(q);
      if (idx >= 0) return 1000 - idx - text.length * 0.1; // substring, earlier and shorter wins
      var ti = 0, qi = 0;                                   // subsequence fallback
      while (ti < text.length && qi < q.length) { if (text[ti] === q[qi]) qi++; ti++; }
      return qi === q.length ? 200 - text.length * 0.1 : -1;
    }

    function render() {
      var q = input.value.trim().toLowerCase();
      results = pages.map(function (p, i) { return { p: p, s: score(q, p.t + " " + p.g), i: i }; })
        .filter(function (r) { return r.s >= 0; })
        .sort(function (a, b) { return b.s - a.s || a.i - b.i; });
      list.innerHTML = "";
      results.forEach(function (r, n) {
        var li = document.createElement("li");
        li.className = "cmdk-item" + (n === 0 ? " is-active" : "");
        li.id = "cmdk-opt-" + n;
        li.setAttribute("role", "option");
        li.setAttribute("aria-selected", n === 0 ? "true" : "false");
        li.dataset.href = r.p.h;
        var t = document.createElement("span"); t.className = "cmdk-t"; t.textContent = r.p.t;
        var g = document.createElement("span"); g.className = "cmdk-g"; g.textContent = r.p.g;
        li.appendChild(t); li.appendChild(g);
        li.addEventListener("click", function () { go(r.p.h); });
        li.addEventListener("mousemove", function () { setActive(n); });
        list.appendChild(li);
      });
      active = 0;
      empty.hidden = results.length > 0;
      list.hidden = results.length === 0;
      updateActive();
    }

    function setActive(n) {
      if (n === active || !results.length) return;
      active = n; updateActive();
    }
    function updateActive() {
      var items = list.children;
      for (var i = 0; i < items.length; i++) {
        var on = i === active;
        items[i].classList.toggle("is-active", on);
        items[i].setAttribute("aria-selected", on ? "true" : "false");
      }
      if (items[active]) {
        input.setAttribute("aria-activedescendant", items[active].id);
        items[active].scrollIntoView({ block: "nearest" });
      } else input.setAttribute("aria-activedescendant", "");
    }
    function go(href) { close(); window.location.href = href; }

    function open() {
      if (!overlay.hidden) return;
      lastFocus = document.activeElement;
      overlay.hidden = false;
      document.body.classList.add("cmdk-on");
      input.value = "";
      render();
      requestAnimationFrame(function () { input.focus(); });
    }
    function close() {
      if (overlay.hidden) return;
      overlay.hidden = true;
      document.body.classList.remove("cmdk-on");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    if (openBtn) openBtn.addEventListener("click", open);
    input.addEventListener("input", render);
    overlay.addEventListener("click", function (e) {
      if (e.target.hasAttribute("data-cmdk-close")) close();
    });
    input.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") { e.preventDefault(); setActive(Math.min(active + 1, results.length - 1)); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive(Math.max(active - 1, 0)); }
      else if (e.key === "Enter") { e.preventDefault(); if (results[active]) go(results[active].p.h); }
      else if (e.key === "Home") { e.preventDefault(); setActive(0); }
      else if (e.key === "End") { e.preventDefault(); setActive(results.length - 1); }
    });
    document.addEventListener("keydown", function (e) {
      if ((e.metaKey || e.ctrlKey) && (e.key === "k" || e.key === "K")) {
        e.preventDefault(); overlay.hidden ? open() : close();
      } else if (e.key === "Escape" && !overlay.hidden) { e.preventDefault(); close(); }
    });
  })();

  // ---- Pick-your-pain-point selector (Home) ----
  (function () {
    var root = document.getElementById("painpoint");
    if (!root) return;
    var tabs = Array.prototype.slice.call(root.querySelectorAll(".pp-chip"));
    var panel = document.getElementById("pp-panel");
    if (!tabs.length || !panel) return;
    var legEl = panel.querySelector("[data-pp-leg]");
    var descEl = panel.querySelector("[data-pp-desc]");
    var linkEl = panel.querySelector("[data-pp-link]");
    var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

    function select(tab, focusPanel) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
      });
      if (legEl) legEl.textContent = tab.dataset.leg;
      if (descEl) descEl.textContent = tab.dataset.desc;
      if (linkEl) { linkEl.setAttribute("href", tab.dataset.href); linkEl.textContent = "See how " + tab.dataset.leg + " helps →"; }
      panel.setAttribute("aria-labelledby", tab.id);
      if (!reduce) { panel.classList.remove("pp-in"); void panel.offsetWidth; panel.classList.add("pp-in"); }
      if (focusPanel) panel.focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab); });
      tab.addEventListener("keydown", function (e) {
        var idx = i;
        if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); idx = (i + 1) % tabs.length; }
        else if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); idx = (i - 1 + tabs.length) % tabs.length; }
        else if (e.key === "Home") { e.preventDefault(); idx = 0; }
        else if (e.key === "End") { e.preventDefault(); idx = tabs.length - 1; }
        else return;
        tabs[idx].focus(); select(tabs[idx]);
      });
    });
  })();

  // ---- Flip cards: tap/keyboard support (hover handled by CSS) ----
  (function () {
    var flips = document.querySelectorAll(".flip");
    if (!flips.length) return;
    var touch = matchMedia("(hover: none)").matches;
    flips.forEach(function (f) {
      function toggle() { f.classList.toggle("is-flipped"); }
      f.addEventListener("click", function (e) {
        if (e.target.closest("a")) return;   // let the More info button work
        if (touch) toggle();
      });
      f.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          if (e.target.closest("a")) return;
          e.preventDefault(); toggle();
        }
      });
    });
  })();


  // ---- Store readiness questionnaire ----
  (function () {
    var form = document.getElementById("quizForm");
    if (!form) return;
    var out = document.getElementById("quizOut"),
        send = document.getElementById("quizSend"),
        field = document.getElementById("quizResult"),
        qs = form.querySelectorAll(".quiz-q");
    var LEGS = {
      turnaround: { t: "Retail Turnaround", href: "/turnaround/",
        d: "Your numbers are not steering the store yet. That is the turnaround starting point: get the trading position honest, stop the bleeding, then rebuild." },
      operations: { t: "Operations and Training", href: "/operations/",
        d: "The store leans on you rather than on standards. That is role definition, training and routines your team can hold without you in the building." },
      analytics: { t: "Analytics and Intelligent Ordering", href: "/analytics/",
        d: "Your stock ledger has not earned trust yet, so ordering is guessing with confidence. Prove presence first, then order against what is really there." }
    };
    function pick(btn) {
      var group = btn.parentNode;
      group.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      score();
    }
    form.querySelectorAll(".quiz-opts button").forEach(function (b) {
      b.setAttribute("aria-pressed", "false");
      b.addEventListener("click", function () { pick(b); });
    });
    function score() {
      var totals = { turnaround: 0, operations: 0, analytics: 0 }, answered = 0, total = 0, max = 0;
      qs.forEach(function (q) {
        var sel = q.querySelector("button[aria-pressed=true]");
        max += 2;
        if (!sel) return;
        answered++;
        var v = parseInt(sel.dataset.v, 10);
        totals[q.dataset.leg] += v; total += v;
      });
      if (answered < qs.length) { out.hidden = true; send.hidden = true; return; }
      var lead = Object.keys(totals).sort(function (a, b) { return totals[b] - totals[a]; })[0];
      var leg = LEGS[lead];
      var pct = Math.round((1 - total / max) * 100);
      var band = pct >= 70 ? "Your systems are carrying you. Tighten the rest."
               : pct >= 40 ? "The pieces are there and the discipline is partial."
               : "The store runs on heroics. Heroics do not scale and do not take leave.";
      out.innerHTML = '<span class="score">' + pct + '% ready</span>' +
        "<h3>Start with " + leg.t + "</h3>" +
        "<p>" + band + " " + leg.d + '</p>' +
        '<p style="margin-top:12px"><a class="more" style="font-weight:600;color:var(--accent-ink)" href="' +
        leg.href + '">See how ' + leg.t + " helps &rarr;</a></p>";
      out.hidden = false; send.hidden = false;
      if (field) field.value = pct + "% ready. Suggested start: " + leg.t +
        " (turnaround " + totals.turnaround + ", operations " + totals.operations + ", analytics " + totals.analytics + ")";
    }
  })();

})();
