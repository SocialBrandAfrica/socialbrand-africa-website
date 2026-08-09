// SocialBrand Method Map: an explorable node graph of the ten methods.
// Reads #methodMap[data-map]. SVG for wide screens, tappable list on mobile.
(function () {
  var el = document.getElementById("methodMap");
  if (!el) return;
  var data;
  try { data = JSON.parse(el.getAttribute("data-map")); } catch (e) { return; }
  if (!data || !data.nodes || !data.nodes.length) return;

  var NS = "http://www.w3.org/2000/svg", W = 1000, H = 560;
  var SHORT = {
    "presence-law": "Presence Law", "8-step-ordering-recipe": "8-Step Recipe",
    "community-rhythm": "Community Rhythm", "capital-velocity": "Capital Velocity",
    "story-test": "Story Test", "two-worlds": "Two Worlds",
    "daily-count-law": "Daily Count Law", "drop-cover": "Drop Cover",
    "base-rate-rule": "Base-Rate Rule", "fit-to-budget": "Fit-to-Budget"
  };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  var bySlug = {}, adj = {};
  data.nodes.forEach(function (n) { bySlug[n.slug] = n; adj[n.slug] = []; });
  data.edges.forEach(function (e) {
    if (adj[e[0]] && adj[e[1]]) { adj[e[0]].push(e[1]); adj[e[1]].push(e[0]); }
  });

  var svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 " + W + " " + H);
  svg.setAttribute("class", "method-map-svg");
  svg.setAttribute("role", "list");
  svg.setAttribute("aria-label", "The ten methods and how they connect. Each node links to its method.");

  var edgeEls = [];
  data.edges.forEach(function (e) {
    var a = bySlug[e[0]], b = bySlug[e[1]];
    if (!a || !b) return;
    var line = document.createElementNS(NS, "line");
    line.setAttribute("x1", a.x); line.setAttribute("y1", a.y);
    line.setAttribute("x2", b.x); line.setAttribute("y2", b.y);
    line.setAttribute("class", "mm-edge");
    line.dataset.a = e[0]; line.dataset.b = e[1];
    svg.appendChild(line); edgeEls.push(line);
  });

  var nodeEls = {};
  data.nodes.forEach(function (n, i) {
    var deg = adj[n.slug].length;
    var r = 30 + Math.min(deg, 4) * 4;
    var a = document.createElementNS(NS, "a");
    a.setAttribute("href", "/method/" + n.slug + "/");
    a.setAttributeNS("http://www.w3.org/1999/xlink", "href", "/method/" + n.slug + "/");
    a.setAttribute("class", "mm-node");
    a.setAttribute("tabindex", "0");
    a.setAttribute("role", "listitem");
    a.setAttribute("aria-label", n.name + ". " + n.tag);
    a.dataset.slug = n.slug;
    a.style.setProperty("--i", i);
    var c = document.createElementNS(NS, "circle");
    c.setAttribute("cx", n.x); c.setAttribute("cy", n.y); c.setAttribute("r", r);
    c.setAttribute("class", "mm-dot");
    a.appendChild(c);
    var label = document.createElementNS(NS, "text");
    label.setAttribute("x", n.x); label.setAttribute("y", n.y + r + 17);
    label.setAttribute("text-anchor", "middle");
    label.setAttribute("class", "mm-label");
    label.textContent = SHORT[n.slug] || n.name;
    a.appendChild(label);
    var title = document.createElementNS(NS, "title");
    title.textContent = n.name + ". " + n.tag;
    a.appendChild(title);
    svg.appendChild(a);
    nodeEls[n.slug] = a;

    a.addEventListener("pointerenter", function () { highlight(n.slug); });
    a.addEventListener("focus", function () { highlight(n.slug); });
    a.addEventListener("pointerleave", clearHi);
    a.addEventListener("blur", clearHi);
    a.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); window.location.href = "/method/" + n.slug + "/"; }
    });
  });

  var defaultCap = "Point at a method to see what it connects to.";
  var caption = document.createElement("p");
  caption.className = "mm-caption";
  caption.setAttribute("aria-live", "polite");
  caption.textContent = defaultCap;

  el.insertBefore(caption, el.firstChild);
  el.insertBefore(svg, el.firstChild);
  el.classList.add("is-enhanced");
  if (reduce) el.classList.add("mm-reduced");

  function highlight(slug) {
    el.classList.add("mm-active");
    Object.keys(nodeEls).forEach(function (s) {
      var on = s === slug || adj[slug].indexOf(s) >= 0;
      nodeEls[s].classList.toggle("is-on", on);
      nodeEls[s].classList.toggle("is-dim", !on);
    });
    edgeEls.forEach(function (l) {
      var on = l.dataset.a === slug || l.dataset.b === slug;
      l.classList.toggle("is-on", on);
      l.classList.toggle("is-dim", !on);
    });
    var n = bySlug[slug];
    caption.innerHTML = "";
    var strong = document.createElement("strong"); strong.textContent = n.name + ". ";
    var span = document.createElement("span"); span.textContent = n.tag;
    caption.appendChild(strong); caption.appendChild(span);
  }
  function clearHi() {
    el.classList.remove("mm-active");
    Object.keys(nodeEls).forEach(function (s) { nodeEls[s].classList.remove("is-on", "is-dim"); });
    edgeEls.forEach(function (l) { l.classList.remove("is-on", "is-dim"); });
    caption.textContent = defaultCap;
  }

  // Enrich the mobile fallback list with one-line definitions.
  var list = el.querySelector(".method-map-list");
  if (list) {
    list.innerHTML = "";
    data.nodes.forEach(function (n) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "/method/" + n.slug + "/"; a.className = "mm-listitem";
      var t = document.createElement("span"); t.className = "mm-li-name"; t.textContent = n.name;
      var d = document.createElement("span"); d.className = "mm-li-tag"; d.textContent = n.tag;
      a.appendChild(t); a.appendChild(d); li.appendChild(a); list.appendChild(li);
    });
  }
})();
