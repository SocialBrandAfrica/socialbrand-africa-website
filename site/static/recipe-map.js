// SocialBrand Recipe Map: the 8-Step Ordering Recipe as an explorable sequence.
// Same visual language as the Method Map: circles, gold on hover, live caption,
// list fallback on small screens. Reads #recipeMap[data-map].
(function () {
  var el = document.getElementById("recipeMap");
  if (!el) return;
  var data;
  try { data = JSON.parse(el.getAttribute("data-map")); } catch (e) { return; }
  if (!data || !data.length) return;

  var NS = "http://www.w3.org/2000/svg", W = 1000, H = 560;
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Two rows of four, second row running back the other way. The numbers carry
  // the direction, so the sweep stays short and the labels stay readable.
  var POS = [
    [140, 165], [370, 165], [600, 165], [830, 165],
    [830, 400], [600, 400], [370, 400], [140, 400]
  ];
  var R = 34;

  var svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 " + W + " " + H);
  svg.setAttribute("class", "method-map-svg");
  svg.setAttribute("role", "list");
  svg.setAttribute("aria-label", "The eight gates of the ordering recipe, in order. Point at a gate to read what it decides.");

  function line(x1, y1, x2, y2, i) {
    var l = document.createElementNS(NS, "line");
    l.setAttribute("x1", x1); l.setAttribute("y1", y1);
    l.setAttribute("x2", x2); l.setAttribute("y2", y2);
    l.setAttribute("class", "mm-edge");
    l.dataset.from = i; l.dataset.to = i + 1;
    svg.appendChild(l);
    return l;
  }

  // edges between consecutive gates
  var edgeEls = [];
  for (var i = 0; i < POS.length - 1; i++) {
    var a = POS[i], b = POS[i + 1];
    var dx = b[0] - a[0], dy = b[1] - a[1];
    var len = Math.sqrt(dx * dx + dy * dy);
    var ux = dx / len, uy = dy / len;
    edgeEls.push(line(a[0] + ux * R, a[1] + uy * R, b[0] - ux * R, b[1] - uy * R, i));
  }

  // in and out anchors
  function anchor(x, y, text, cls) {
    var g = document.createElementNS(NS, "g");
    g.setAttribute("class", "rm-anchor " + (cls || ""));
    var t = document.createElementNS(NS, "text");
    t.setAttribute("x", x); t.setAttribute("y", y);
    t.setAttribute("text-anchor", "middle");
    t.setAttribute("class", "rm-anchor-t");
    t.textContent = text;
    g.appendChild(t);
    svg.appendChild(g);
  }
  anchor(140, 78, "Every line in the range");
  anchor(140, 500, "An order that explains itself", "is-out");

  var nodeEls = [];
  data.forEach(function (n, i) {
    var p = POS[i];
    var g = document.createElementNS(NS, "g");
    g.setAttribute("class", "mm-node rm-node" + (n.key ? " is-key" : ""));
    g.setAttribute("tabindex", "0");
    g.setAttribute("role", "listitem");
    g.setAttribute("aria-label", "Gate " + (i + 1) + ". " + n.name + ". " + n.what);
    g.style.setProperty("--i", i);

    var c = document.createElementNS(NS, "circle");
    c.setAttribute("cx", p[0]); c.setAttribute("cy", p[1]); c.setAttribute("r", R);
    c.setAttribute("class", "mm-dot");
    g.appendChild(c);

    var num = document.createElementNS(NS, "text");
    num.setAttribute("x", p[0]); num.setAttribute("y", p[1] + 8);
    num.setAttribute("text-anchor", "middle");
    num.setAttribute("class", "rm-num");
    num.textContent = i + 1;
    g.appendChild(num);

    var label = document.createElementNS(NS, "text");
    label.setAttribute("x", p[0]); label.setAttribute("y", p[1] + R + 22);
    label.setAttribute("text-anchor", "middle");
    label.setAttribute("class", "mm-label");
    label.textContent = n.name;
    g.appendChild(label);

    var title = document.createElementNS(NS, "title");
    title.textContent = n.name + ". " + n.what;
    g.appendChild(title);

    svg.appendChild(g);
    nodeEls.push(g);

    g.addEventListener("pointerenter", function () { show(i); });
    g.addEventListener("focus", function () { show(i); });
    g.addEventListener("pointerleave", clear);
    g.addEventListener("blur", clear);
  });

  var defaultCap = "Point at a gate to see what it decides.";
  var caption = document.createElement("p");
  caption.className = "mm-caption";
  caption.setAttribute("aria-live", "polite");
  caption.textContent = defaultCap;

  el.insertBefore(caption, el.firstChild);
  el.insertBefore(svg, el.firstChild);
  el.classList.add("is-enhanced");
  if (reduce) el.classList.add("mm-reduced");

  function show(i) {
    el.classList.add("mm-active");
    nodeEls.forEach(function (g, j) {
      g.classList.toggle("is-on", j === i);
      g.classList.toggle("is-dim", j !== i);
    });
    edgeEls.forEach(function (l) {
      var on = +l.dataset.from === i || +l.dataset.to === i;
      l.classList.toggle("is-on", on);
      l.classList.toggle("is-dim", !on);
    });
    var n = data[i];
    caption.innerHTML = "";
    var s = document.createElement("strong");
    s.textContent = (i + 1) + ". " + n.name + ". ";
    var span = document.createElement("span");
    span.textContent = n.what;
    caption.appendChild(s); caption.appendChild(span);
  }
  function clear() {
    el.classList.remove("mm-active");
    nodeEls.forEach(function (g) { g.classList.remove("is-on", "is-dim"); });
    edgeEls.forEach(function (l) { l.classList.remove("is-on", "is-dim"); });
    caption.textContent = defaultCap;
  }

  // small-screen fallback list
  var list = el.querySelector(".method-map-list");
  if (list) {
    list.innerHTML = "";
    data.forEach(function (n, i) {
      var li = document.createElement("li");
      var d = document.createElement("div");
      d.className = "mm-listitem" + (n.key ? " is-key" : "");
      var t = document.createElement("span");
      t.className = "mm-li-name";
      t.textContent = (i + 1) + ". " + n.name;
      var tag = document.createElement("span");
      tag.className = "mm-li-tag";
      tag.textContent = n.what;
      d.appendChild(t); d.appendChild(tag); li.appendChild(d); list.appendChild(li);
    });
  }
})();
