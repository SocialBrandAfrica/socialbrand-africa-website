// SocialBrand fx layer: scrollytelling, magnetic buttons, cursor glow, hero parallax.
// Progressive enhancement only. Everything degrades to static under reduced motion.
(function () {
  var mq = function (q) { return window.matchMedia ? matchMedia(q).matches : false; };
  var reduce = mq("(prefers-reduced-motion: reduce)");
  var fine = mq("(pointer: fine)") && !mq("(hover: none)");
  var clamp = function (v, min, max) { return Math.max(min, Math.min(max, v)); };

  // ---------- Scrollytelling ----------
  (function () {
    var blocks = document.querySelectorAll("[data-scrolly]");
    if (!blocks.length) return;
    blocks.forEach(function (b) {
      var steps = Array.prototype.slice.call(b.querySelectorAll(":scope > p"));
      if (!steps.length) return;
      var rail = document.createElement("span"); rail.className = "scrolly-rail";
      var fill = document.createElement("span"); fill.className = "scrolly-fill";
      rail.appendChild(fill); b.appendChild(rail);
      b.classList.add("scrolly-ready");

      if (reduce || !("IntersectionObserver" in window)) {
        steps.forEach(function (s) { s.classList.add("on"); });
        fill.style.height = "100%";
        return;
      }
      steps.forEach(function (s) { s.classList.add("scrolly-step"); });
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) e.target.classList.add("on"); });
      }, { threshold: 0.55, rootMargin: "0px 0px -12% 0px" });
      steps.forEach(function (s) { io.observe(s); });

      var ticking = false;
      function draw() {
        ticking = false;
        var r = b.getBoundingClientRect(), vh = window.innerHeight || 1;
        var prog = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.35), 0, 1);
        var done = b.querySelectorAll(".scrolly-step.on").length;
        var stepProg = done / steps.length;
        fill.style.height = (Math.max(prog, stepProg) * 100).toFixed(1) + "%";
      }
      function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(draw); } }
      window.addEventListener("scroll", onScroll, { passive: true });
      window.addEventListener("resize", onScroll, { passive: true });
      draw();
    });
  })();

  // ---------- Hero parallax + entrance flag ----------
  (function () {
    var hero = document.querySelector(".hero");
    if (!hero) return;
    hero.classList.add("hero-fx");
    if (reduce) return;
    var ticking = false;
    function draw() {
      ticking = false;
      var y = window.pageYOffset || 0;
      hero.style.setProperty("--sky-shift", (y * 0.16).toFixed(1) + "px");
      hero.style.setProperty("--aurora-shift", (y * 0.08).toFixed(1) + "px");
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(draw); }
    }, { passive: true });
    draw();
  })();

  // ---------- Magnetic buttons (pointer + motion only) ----------
  if (fine && !reduce) {
    document.querySelectorAll(".btn").forEach(function (btn) {
      btn.addEventListener("pointermove", function (e) {
        var r = btn.getBoundingClientRect();
        var mx = clamp((e.clientX - (r.left + r.width / 2)) * 0.28, -7, 7);
        var my = clamp((e.clientY - (r.top + r.height / 2)) * 0.4, -6, 6);
        btn.style.transform = "translate(" + mx.toFixed(2) + "px," + (my - 1).toFixed(2) + "px)";
      });
      btn.addEventListener("pointerleave", function () { btn.style.transform = ""; });
      btn.addEventListener("blur", function () { btn.style.transform = ""; });
    });
  }

  // ---------- Cursor glow on hero / CTA surfaces ----------
  if (fine && !reduce) {
    document.querySelectorAll(".hero, .hero-page, .cta-band").forEach(function (sec) {
      var glow = document.createElement("span");
      glow.className = "pointer-glow"; glow.setAttribute("aria-hidden", "true");
      sec.insertBefore(glow, sec.firstChild);
      sec.addEventListener("pointermove", function (e) {
        var r = sec.getBoundingClientRect();
        glow.style.setProperty("--gx", (e.clientX - r.left) + "px");
        glow.style.setProperty("--gy", (e.clientY - r.top) + "px");
        glow.style.opacity = "1";
      });
      sec.addEventListener("pointerleave", function () { glow.style.opacity = "0"; });
    });
  }
})();
