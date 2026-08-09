/* SocialBrand demo dashboard. Reads window.DEMO_DATA (generated, fictional).
   Vanilla JS, Chart.js only. Every control recomputes from the shipped dataset. */
(function () {
  "use strict";
  var D = window.DEMO_DATA, body = document.getElementById("dashBody");
  if (!D || !body) return;

  var charts = [];
  var REDUCE = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------- state */
  var S = {
    view: "rhythm",
    rh: { store: "all", period: "30", gran: "daily" },
    mv: { store: "all", by: "units", set: "movers", reasons: false },
    stk: { store: "all", filter: "all", reasons: true },
    cap: { mode: "pure" },
    ord: {
      store: "all", desk: "dry", preset: "standard", basis: "normal", fit: "on",
      del: D.order.dates[0].v, nxt: D.order.dates[2].v, stamp: 0
    }
  };

  /* ------------------------------------------------------------- helpers */
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }
  function moneyC(n) {
    var a = Math.abs(n);
    if (a >= 1e6) return "$" + (n / 1e6).toFixed(2) + "M";
    if (a >= 1e3) return "$" + (n / 1e3).toFixed(1) + "k";
    return money(n);
  }
  function money2(n) { return "$" + n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function int(n) { return Math.round(n).toLocaleString("en-US"); }
  function d1(n) { return n.toLocaleString("en-US", { minimumFractionDigits: 1, maximumFractionDigits: 1 }); }
  function d2(n) { return n.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  function pct(n) { return (n > 0 ? "+" : "") + d1(n) + "%"; }
  function deltaCls(n) { return n >= 2 ? "dx-up" : (n <= -8 ? "dx-dn" : (n < 0 ? "dx-fl" : "dx-nt")); }
  function deltaHTML(n) { return '<span class="' + deltaCls(n) + '">' + pct(n) + "</span>"; }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function storeName(v) { return v === "sm" ? "Fairview SuperMart" : v === "lq" ? "Fairview Liquor" : "All stores"; }
  function days(period) { return period === "all" ? D.sales.labels.length : parseInt(period, 10); }
  function sum(a) { var t = 0, i; for (i = 0; i < a.length; i++) t += a[i]; return t; }
  function tail(a, n) { return a.slice(a.length - n); }
  function head(a, n, off) {
    var end = a.length - off, start = Math.max(0, end - n);
    return end > 0 ? a.slice(start, end) : [];
  }

  function storeSeries(store) {
    var sm = D.sales.sm, lq = D.sales.lq, out = [], i;
    if (store === "sm") return sm.slice();
    if (store === "lq") return lq.slice();
    for (i = 0; i < sm.length; i++) out.push(sm[i] + lq[i]);
    return out;
  }
  function basketSeries(store) {
    var a = D.sales.bsm, b = D.sales.blq, out = [], i;
    if (store === "sm") return a.slice();
    if (store === "lq") return b.slice();
    for (i = 0; i < a.length; i++) out.push(a[i] + b[i]);
    return out;
  }

  function chips(label, items, current, act) {
    return '<div class="dx-grp" role="group" aria-label="' + esc(label) + '"><span class="dx-lab">' + esc(label) + "</span>" +
      items.map(function (i) {
        return '<button type="button" class="dx-chip" data-act="' + act + '" data-val="' + i.v +
          '" aria-pressed="' + (String(i.v) === String(current)) + '">' + esc(i.t) + "</button>";
      }).join("") + "</div>";
  }
  function seg(label, items, current, act) {
    return '<div class="dx-seg" role="group" aria-label="' + esc(label) + '">' +
      items.map(function (i) {
        return '<button type="button" data-act="' + act + '" data-val="' + i.v +
          '" aria-pressed="' + (String(i.v) === String(current)) + '">' + esc(i.t) + "</button>";
      }).join("") + "</div>";
  }
  function selectField(label, items, current, act) {
    return '<label class="dx-field"><span class="dx-lab">' + esc(label) + '</span><select data-act="' + act + '">' +
      items.map(function (i) {
        return '<option value="' + i.v + '"' + (i.v === current ? " selected" : "") + ">" + esc(i.t) + "</option>";
      }).join("") + "</select></label>";
  }
  function kpi(v, k, delta, why) {
    return '<div class="kpi"><div class="v">' + v + "</div>" +
      (delta ? '<div class="d">' + delta + "</div>" : "") +
      '<div class="k">' + esc(k) + "</div>" +
      (why ? '<details><summary class="why">why this number</summary><div class="reason">' + why + "</div></details>" : "") +
      "</div>";
  }
  function bar(frac, clay) {
    var w = Math.max(0, Math.min(1, frac)) * 100;
    return '<span class="dx-bar' + (clay ? " cl" : "") + '"><i style="width:' + w.toFixed(1) + '%"></i></span>';
  }
  function reason(t) { return '<div class="dx-why"><div class="reason">' + t + "</div></div>"; }

  function card(title, sub, right, inner, cls) {
    return '<div class="dx-card' + (cls ? " " + cls : "") + '"><div class="dx-card-h"><h3>' + title + "</h3>" +
      (sub ? '<span class="sub">' + sub + "</span>" : "") +
      (right ? '<span class="sp">' + right + "</span>" : "") +
      "</div>" + inner + "</div>";
  }

  function chartColors() {
    var dark = document.documentElement.dataset.theme === "dark";
    return {
      grid: dark ? "rgba(255,255,255,.07)" : "rgba(90,60,25,.10)",
      tick: dark ? "#b6a68d" : "#6f6353",
      gold: "#bf8a2c", gold2: "#e3b85a",
      clay: dark ? "#dd8763" : "#c15b3c",
      slow: dark ? "#a98a52" : "#bfa06a",
      dead: dark ? "#e2705c" : "#c0392b"
    };
  }
  function mkChart(id, cfg) {
    var el = document.getElementById(id);
    if (!el || !window.Chart) return;
    cfg.options = cfg.options || {};
    cfg.options.animation = REDUCE ? false : cfg.options.animation;
    charts.push(new Chart(el, cfg));
  }

  /* ============================================================ SALES RHYTHM */
  function viewRhythm() {
    var st = S.rh.store, n = days(S.rh.period), full = storeSeries(st), bk = basketSeries(st);
    var cur = tail(full, n), prev = head(full, n, n);
    var curT = sum(cur), prevT = sum(prev);
    var curAvg = cur.length ? curT / cur.length : 0, prevAvg = prev.length ? prevT / prev.length : 0;
    var gr = prevAvg ? ((curAvg - prevAvg) / prevAvg) * 100 : null;
    var baskets = sum(tail(bk, n)), avgBasket = baskets ? curT / baskets : 0;
    var yest = full[full.length - 1], lastWeek = full[full.length - 8];
    var yestD = lastWeek ? ((yest - lastWeek) / lastWeek) * 100 : 0;
    var marg = st === "sm" ? D.meta.margin.sm : st === "lq" ? D.meta.margin.lq
      : (D.meta.margin.sm * 0.72 + D.meta.margin.lq * 0.28);
    var margLY = st === "lq" ? D.meta.margin.lqly : D.meta.margin.smly;
    var best = 0, bestI = 0, i;
    for (i = 0; i < cur.length; i++) if (cur[i] > best) { best = cur[i]; bestI = i; }
    var labels = tail(D.sales.labels, n);
    var from = labels[0], to = labels[labels.length - 1];

    var rail = '<div class="dx-rail">' +
      chips("Stores", D.meta.stores, st, "rh.store") +
      chips("Period", D.meta.periods, S.rh.period, "rh.period") +
      seg("Chart granularity", [{ v: "daily", t: "Daily" }, { v: "weekly", t: "Weekly" }], S.rh.gran, "rh.gran") +
      "</div>";

    var ctx = '<p class="dx-ctx"><b>' + storeName(st) + "</b> &middot; " + from + " to " + to + " " +
      D.meta.last.slice(-4) + " (" + n + " trading days, " + D.meta.snapshots + " snapshots) &middot; all departments &middot; all items &middot; figures exclude sales tax</p>";

    var kpis = '<div class="dx-kpis">' +
      kpi(moneyC(curT), "Sales, period",
        gr === null ? '<span class="dx-nt">whole season in view</span>' : deltaHTML(gr) + " a day vs prior window",
        "Till sales for the days in view, read straight from the sales ledger and never from a manual capture. The comparison runs on the daily average against the window immediately before, so a payday week is never quietly compared to a mid-month one.") +
      kpi(money(yest), "Sales yesterday", deltaHTML(yestD) + " vs same day last week",
        "The last full trading day. It is compared to the same weekday a week back, because a Tuesday and a Saturday in this town are two different businesses.") +
      kpi(int(baskets), "Baskets", "average basket " + money2(avgBasket),
        "Till slips, not units. Sales can rise on fewer, bigger baskets or on more, smaller ones, and the two ask for opposite decisions on the floor.") +
      kpi(d1(marg) + "%", "Gross margin", deltaHTML(margLY) + " pts vs last year",
        "Margin measured after the cost errors on the stock ledger were taken out. Margin calculated on a wrong cost is a rumour, not a measurement.") +
      kpi(labels[bestI], "Best day", money(best),
        "The strongest single day in view. It sits in the wage window every month, which is why depth is built before it rather than reported after it.") +
      "</div>";

    var chart = '<div class="dx-card"><div class="dx-card-h"><h3>Daily trading rhythm</h3>' +
      '<span class="sub">' + (st === "all" ? "both stores" : storeName(st)) + " &middot; " + (S.rh.gran === "daily" ? "day by day" : "week by week") + "</span>" +
      '<span class="sp"><span class="dx-tag">Ex-tax</span></span></div>' +
      '<div class="chart-box"><canvas id="rhythmChart" aria-label="Daily sales for the selected stores"></canvas></div>' +
      '<div class="reason" style="margin-top:14px"><b>Read the shape.</b> The tall bands are the wage window at month end, the early-month shelf is grant money, and Friday and Saturday carry the week. A store ordered off a flat average starves exactly where this curve peaks.</div></div>';

    /* departments */
    var depts = D.depts.filter(function (d) { return st === "all" || d.st === st; });
    var storeTotals = {};
    storeTotals.sm = sum(tail(D.sales.sm, n));
    storeTotals.lq = sum(tail(D.sales.lq, n));
    var rows = depts.map(function (d) {
      return { n: d.n, st: d.st, v: storeTotals[d.st] * d.sh, ly: d.ly[S.rh.period] };
    }).sort(function (a, b) { return b.v - a.v; });
    var maxV = rows.length ? rows[0].v : 1;
    var deptHTML = rows.map(function (r) {
      var why = D.deptWhy[r.n] || "Tracking close to last year. The department is doing what it did, which is worth knowing before anybody changes it.";
      return '<div class="dx-dept"><span class="nm">' + esc(r.n) + "</span>" +
        '<span class="vl">' + moneyC(r.v) + "</span>" +
        '<span class="dl ' + deltaCls(r.ly) + '">' + pct(r.ly) + "</span>" +
        '<span class="bw">' + bar(r.v / maxV, r.ly <= -8) + "</span>" +
        '<details class="dx-why"><summary class="why">why</summary><div class="reason">' + why + "</div></details></div>";
    }).join("");
    var deptCard = card("Sales by department",
      rows.length + " departments &middot; against the same period last year",
      '<span class="dx-tag">Ex-tax</span>',
      deptHTML + '<p class="dx-note">Green is ahead of last year, amber is slightly behind, red is far enough behind to need a reason before the next order is placed.</p>');

    body.innerHTML = rail + ctx + kpis + chart + deptCard;

    var c = chartColors();
    if (S.rh.gran === "daily") {
      var ds = [];
      if (st === "all" || st === "sm") ds.push({ label: "SuperMart", data: tail(D.sales.sm, n), borderColor: c.gold, backgroundColor: "transparent", borderWidth: 2, pointRadius: 0, tension: .25 });
      if (st === "all" || st === "lq") ds.push({ label: "Liquor", data: tail(D.sales.lq, n), borderColor: c.clay, backgroundColor: "transparent", borderWidth: 2, pointRadius: 0, tension: .25 });
      mkChart("rhythmChart", {
        type: "line",
        data: { labels: labels, datasets: ds },
        options: {
          responsive: true, maintainAspectRatio: false, interaction: { mode: "index", intersect: false },
          plugins: {
            legend: { labels: { color: c.tick, boxWidth: 12 } },
            tooltip: { callbacks: { label: function (x) { return x.dataset.label + ": " + money(x.parsed.y); } } }
          },
          scales: {
            x: { ticks: { color: c.tick, maxTicksLimit: 9 }, grid: { display: false } },
            y: { ticks: { color: c.tick, callback: function (v) { return "$" + Math.round(v / 1000) + "k"; } }, grid: { color: c.grid } }
          }
        }
      });
    } else {
      var wl = [], ws = [], wq = [], k, j, a = tail(D.sales.sm, n), b = tail(D.sales.lq, n), lb = labels;
      for (k = a.length; k > 0; k -= 7) {
        var s0 = Math.max(0, k - 7), ss = 0, ll = 0;
        for (j = s0; j < k; j++) { ss += a[j]; ll += b[j]; }
        wl.unshift("w/e " + lb[k - 1]); ws.unshift(ss); wq.unshift(ll);
      }
      var wds = [];
      if (st === "all" || st === "sm") wds.push({ label: "SuperMart", data: ws, backgroundColor: c.gold, borderRadius: 4 });
      if (st === "all" || st === "lq") wds.push({ label: "Liquor", data: wq, backgroundColor: c.clay, borderRadius: 4 });
      mkChart("rhythmChart", {
        type: "bar",
        data: { labels: wl, datasets: wds },
        options: {
          responsive: true, maintainAspectRatio: false,
          plugins: {
            legend: { labels: { color: c.tick, boxWidth: 12 } },
            tooltip: { callbacks: { label: function (x) { return x.dataset.label + ": " + money(x.parsed.y); } } }
          },
          scales: {
            x: { stacked: true, ticks: { color: c.tick, maxTicksLimit: 10 }, grid: { display: false } },
            y: { stacked: true, ticks: { color: c.tick, callback: function (v) { return "$" + Math.round(v / 1000) + "k"; } }, grid: { color: c.grid } }
          }
        }
      });
    }
  }

  /* ============================================================== TOP MOVERS */
  function moverRows() {
    var n = 30, mv = S.mv;
    return D.prods.filter(function (p) {
      return (mv.store === "all" || p.st === mv.store) && (mv.set === "movers" ? !p.nm : !!p.nm);
    }).map(function (p) {
      var units = p.r * n * p.mx[0];
      var rate = units / n;
      var cover = rate > 0 ? p.oh / rate : 999;
      return { p: p, units: units, value: units * p.p, rate: rate, cover: cover };
    }).sort(function (a, b) {
      return S.mv.by === "value" ? b.value - a.value : b.units - a.units;
    });
  }
  function moverWhy(r) {
    var p = r.p;
    if (p.nm) {
      return "Sold " + int(r.units) + " units in the last 30 days at " + d2(r.rate) + " a day. The stock behind it outlasts anything that rate can justify, so this is a capital question and an exit question, not an ordering one.";
    }
    if (r.cover < 1.6) {
      return "Selling faster than it is being replaced. Cover on hand runs " + d1(r.cover) + " days, so the shelf empties before the next delivery unless the order reads the rate rather than the last order.";
    }
    if (r.cover > 5) {
      return "Sells steadily, and there is more behind it than the rate needs. Nothing is broken, it simply does not need depth added this week, and the money is better spent on the lines above it.";
    }
    return "Rate and cover agree. Bought to what it sells, replaced before it gaps. This is what the rest of the range is being measured against.";
  }
  function viewMovers() {
    var rows = moverRows(), showing = S.mv.set === "movers" ? rows.slice(0, 20) : rows;
    var totUnits = 0, totVal = 0;
    rows.forEach(function (r) { totUnits += r.units; totVal += r.value; });

    var rail = '<div class="dx-rail">' +
      chips("Stores", D.meta.stores, S.mv.store, "mv.store") +
      seg("Rank by", [{ v: "units", t: "By units" }, { v: "value", t: "By value" }], S.mv.by, "mv.by") +
      seg("Set", [{ v: "movers", t: "Movers" }, { v: "slow", t: "Non-movers" }], S.mv.set, "mv.set") +
      seg("Reasons", [{ v: "1", t: "Reasons on" }, { v: "0", t: "Off" }], S.mv.reasons ? "1" : "0", "mv.reasons") +
      '<span class="dx-search"><span class="dx-lab">Find</span><input type="search" id="mvSearch" placeholder="Product name" aria-label="Search products by name"></span>' +
      "</div>";

    var ctx = '<p class="dx-ctx"><b>' + storeName(S.mv.store) + "</b> &middot; last 30 days &middot; " +
      (S.mv.set === "movers" ? "top " + showing.length + " by " + (S.mv.by === "value" ? "value" : "units") : rows.length + " lines that have stopped moving") +
      " &middot; <span id='mvCount'>" + showing.length + " shown</span></p>";

    var headHTML = '<div class="dx-head"><span>#</span><span>Product</span><span class="r">Units</span><span class="r">Value</span><span class="r">Cover</span><span class="r">Avg/day</span></div>';
    var rowsHTML = showing.map(function (r, i) {
      var cls = r.p.nm ? "bad" : r.cover < 1.6 ? "warn" : "";
      return '<div class="dx-row ' + cls + '" data-name="' + esc(r.p.n.toLowerCase()) + '">' +
        '<span class="dx-rank">' + (i + 1) + "</span>" +
        '<span class="dx-id"><b>' + esc(r.p.n) + '</b><span class="dx-sub">' + esc(r.p.d) + " &middot; " + esc(r.p.pk) + "</span></span>" +
        '<span class="dx-figs">' +
        '<span class="dx-fig acc"><i>Units</i><b>' + int(r.units) + "</b></span>" +
        '<span class="dx-fig"><i>Value</i><b>' + moneyC(r.value) + "</b></span>" +
        '<span class="dx-fig mut"><i>Cover</i><b>' + (r.cover > 900 ? "none" : d1(r.cover) + "d") + "</b></span>" +
        '<span class="dx-fig mut"><i>Avg/day</i><b>' + d2(r.rate) + " u/d</b></span></span>" +
        (S.mv.reasons ? reason(moverWhy(r)) : "") +
        "</div>";
    }).join("");

    var inner = headHTML + '<div id="mvRows">' + rowsHTML + '</div><p class="dx-empty" id="mvEmpty" hidden>No product in this set matches that name.</p>' +
      '<p class="dx-note">Cover is how many days the stock on hand lasts at the rate the line actually sells, not at the rate anybody hoped it would.</p>';

    body.innerHTML = rail + ctx +
      card(S.mv.set === "movers" ? "Top 20 movers" : "Lines that have stopped",
        int(totUnits) + " units &middot; " + moneyC(totVal) + " across the set",
        '<span class="dx-tag">Ex-tax</span>', inner, "dx-t-mov");

    var q = document.getElementById("mvSearch");
    if (q) q.addEventListener("input", function () {
      var v = q.value.trim().toLowerCase(), shown = 0;
      Array.prototype.forEach.call(document.querySelectorAll("#mvRows .dx-row"), function (el) {
        var hit = !v || el.getAttribute("data-name").indexOf(v) > -1;
        el.hidden = !hit; if (hit) shown++;
      });
      var c = document.getElementById("mvCount"), e = document.getElementById("mvEmpty");
      if (c) c.textContent = shown + " shown";
      if (e) e.hidden = shown > 0;
    });
  }

  /* ============================================================ STOCK HEALTH */
  function viewStock() {
    var f = S.stk.filter, st = S.stk.store;
    var all = D.stock.filter(function (r) { return st === "all" || r.st === st; });
    var rows = all.filter(function (r) { return f === "all" || r.tag === f; });
    var atRisk = 0, repairs = 0, counts = 0;
    all.forEach(function (r) {
      if (r.tag === "phantom" || r.tag === "count" || r.tag === "cost") atRisk += r.val;
      if (r.tag === "neg" || r.tag === "cost") repairs++;
      if (r.tag === "count") counts++;
    });

    var rail = '<div class="dx-rail">' +
      chips("Stores", D.meta.stores, st, "stk.store") +
      chips("Verdict", D.stockFilters, f, "stk.filter") +
      seg("Reasons", [{ v: "1", t: "Reasons on" }, { v: "0", t: "Off" }], S.stk.reasons ? "1" : "0", "stk.reasons") +
      "</div>";

    var ctx = '<p class="dx-ctx"><b>' + storeName(st) + "</b> &middot; " + all.length + " lines surfaced from a range of 9,400 &middot; " +
      rows.length + " in this filter &middot; ledger read to close of trade " + D.meta.last + "</p>";

    var kpis = '<div class="dx-kpis">' +
      kpi(int(all.length), "Lines surfaced", "",
        "Out of a range of 9,400, these are the lines whose ledger story stopped making sense. Every one arrives with that story attached, because a flag without a reason just becomes noise somebody learns to ignore.") +
      kpi(int(repairs), "Ledger repairs", "",
        "Breaks that are fixed at source in the store's own system, not adjusted away here. Zeroing a negative hides the disease and keeps the symptom.") +
      kpi(int(counts), "Count first", "",
        "Claims that have aged past the point where behaviour still proves them. They go onto the count list before any order is allowed to trust them, ranked by the money at risk.") +
      kpi(moneyC(atRisk), "Capital under question", "",
        "The money sitting behind claims that cannot yet prove themselves. It is not written off, it is counted. Until then it does not get to steer a decision.") +
      "</div>";

    var headHTML = '<div class="dx-head"><span>#</span><span>Product</span><span class="r">Book qty</span><span class="r">At cost</span><span class="r">Verdict</span></div>';
    var rowsHTML = rows.length ? rows.map(function (r, i) {
      var cls = r.pill[0] === "red" ? "bad" : r.pill[0] === "amber" ? "warn" : "good";
      return '<div class="dx-row ' + cls + '">' +
        '<span class="dx-rank">' + (i + 1) + "</span>" +
        '<span class="dx-id"><b>' + esc(r.n) + '</b><span class="dx-sub">' + esc(r.d) + " &middot; " + esc(r.pk) + " &middot; code " + esc(r.c) + "</span></span>" +
        '<span class="dx-figs">' +
        '<span class="dx-fig ' + (r.qty < 0 ? "neg" : "") + '"><i>Book qty</i><b>' + int(r.qty) + "</b></span>" +
        '<span class="dx-fig mut"><i>At cost</i><b>' + (r.val ? moneyC(r.val) : "n/a") + "</b></span></span>" +
        '<span class="dx-verdict"><span class="pill ' + r.pill[0] + '">' + esc(r.pill[1]) + "</span></span>" +
        (S.stk.reasons ? reason(r.story) : "") +
        "</div>";
    }).join("") : '<p class="dx-empty">Nothing in this store matches that verdict, which is the answer you want.</p>';

    body.innerHTML = rail + ctx + kpis +
      card("Lines under question", rows.length + " lines &middot; ranked by how loudly the ledger is arguing with itself",
        '<span class="dx-tag">Book qty</span>',
        headHTML + rowsHTML +
        '<p class="dx-note">A line is known present only when recent behaviour or a recent count says so. Everything else is a claim, and a claim is not stock.</p>',
        "dx-t-stock");
  }

  /* ================================================================ CAPITAL */
  function viewCapital() {
    var C = D.capital, m = S.cap.mode, cur = m === "pure" ? C.pure : C.raw, c = chartColors();
    var gapTotal = C.raw.total - C.pure.total;
    var workPct = (cur.working / cur.total) * 100;

    var rail = '<div class="dx-rail">' +
      seg("Capital basis", [{ v: "raw", t: "Raw ledger" }, { v: "pure", t: "Purified" }], m, "cap.mode") +
      "</div>";

    var ctx = '<p class="dx-ctx"><b>' + cur.label + "</b> &middot; both stores &middot; stock at cost &middot; " +
      (m === "pure" ? "invented cost, unproven claims and deposit balances removed" : "every claim taken at face value, nothing tested") + "</p>";

    var kpis = '<div class="dx-kpis">' +
      kpi(moneyC(cur.total), "Stock at cost", "", cur.why) +
      kpi(d1(workPct) + "%", "Working", "",
        "The share of this money on lines that are selling and replacing themselves. This is the part doing its job, and the only part that should feel comfortable.") +
      kpi(moneyC(cur.slow), "Slow", "",
        "Still selling, far slower than it was bought. Slow stock is not a write-off, it is a buying decision that has not been corrected yet.") +
      kpi(moneyC(cur.dead), "Dead", "",
        "No sales in its own horizon. Rent paid on regret. It gets an exit plan and a date, never another order.") +
      "</div>";

    var chart = '<div class="dx-card"><div class="dx-card-h"><h3>Where the money is standing</h3>' +
      '<span class="sub">' + cur.label.toLowerCase() + "</span></div>" +
      '<div class="chart-box" style="max-width:380px;margin:0 auto"><canvas id="capChart" aria-label="Capital split between working, slow and dead stock"></canvas></div>' +
      '<div class="dx-legend"><span><i style="background:' + c.gold + '"></i>Working ' + moneyC(cur.working) + "</span>" +
      '<span><i style="background:' + c.slow + '"></i>Slow ' + moneyC(cur.slow) + "</span>" +
      '<span><i style="background:' + c.dead + '"></i>Dead ' + moneyC(cur.dead) + "</span></div></div>";

    var gapRows = C.gap.map(function (g) {
      return '<div class="dx-dept"><span class="nm">' + esc(g.n) + "</span>" +
        '<span class="vl">' + moneyC(g.v) + "</span>" +
        '<span class="dl dx-nt">' + d1((g.v / gapTotal) * 100) + "%</span>" +
        '<span class="bw">' + bar(g.v / gapTotal, true) + "</span>" +
        '<details class="dx-why"><summary class="why">why</summary><div class="reason">' + g.why + "</div></details></div>";
    }).join("");
    var gapCard = card("Raw against purified",
      moneyC(gapTotal) + " of the raw claim never was stock",
      '<span class="dx-tag">At cost</span>',
      gapRows + '<div class="reason" style="margin-top:12px"><b>Why the two numbers differ.</b> Most of the dead capital in a broken ledger was never stock at all. It was arithmetic, an unproven claim, or money that belongs in a deposit account. Purify first, then manage what is actually there. Switch the control above and watch which decisions would have been made on the wrong number.</div>');

    var offHead = '<div class="dx-head"><span>#</span><span>Line</span><span class="r">Capital tied</span><span class="r">Since last sale</span></div>';
    var offRows = C.offenders.slice().sort(function (a, b) { return b.v - a.v; }).map(function (o, i) {
      return '<div class="dx-row ' + (o.days > 120 ? "bad" : "warn") + '">' +
        '<span class="dx-rank">' + (i + 1) + "</span>" +
        '<span class="dx-id"><b>' + esc(o.n) + '</b><span class="dx-sub">' + esc(o.d) + " &middot; " + esc(o.pk) + "</span></span>" +
        '<span class="dx-figs"><span class="dx-fig"><i>Capital tied</i><b>' + moneyC(o.v) + "</b></span>" +
        '<span class="dx-fig mut"><i>Since last sale</i><b>' + o.days + " days</b></span></span>" +
        reason(o.why) + "</div>";
    }).join("");
    var offCard = card("Biggest capital offenders", "ranked by money standing still",
      "", offHead + offRows +
      '<p class="dx-note">Each line leaves with a decision attached: count it, fix its cost, clear it, or leave it alone on purpose.</p>',
      "dx-t-cap");

    body.innerHTML = rail + ctx + kpis + '<div class="dx-cols">' + chart + gapCard + "</div>" + offCard;

    mkChart("capChart", {
      type: "doughnut",
      data: {
        labels: ["Working", "Slow", "Dead"],
        datasets: [{ data: [cur.working, cur.slow, cur.dead], backgroundColor: [c.gold, c.slow, c.dead], borderWidth: 0 }]
      },
      options: {
        responsive: true, maintainAspectRatio: false, cutout: "64%",
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: function (x) { return x.label + ": " + money(x.parsed); } } }
        }
      }
    });
  }

  /* =============================================================== ORDERING */
  function deskById(v) {
    var d = D.order.desks, i;
    for (i = 0; i < d.length; i++) if (d[i].v === v) return d[i];
    return d[0];
  }
  function dateLabel(v) {
    var d = D.order.dates, i;
    for (i = 0; i < d.length; i++) if (d[i].v === v) return d[i].t;
    return v;
  }
  function gapDays(a, b) {
    return Math.max(1, Math.round((Date.parse(b) - Date.parse(a)) / 86400000));
  }

  function computeOrder() {
    var o = S.ord, desk = deskById(o.desk);
    var gap = gapDays(o.del, o.nxt), horizon = gap + 2;
    var pf = {
      standard: { kvi: 1, core: 1, flex: 1 },
      essential: { kvi: 1, core: 0.72, flex: 0 },
      catchup: { kvi: 1.15, core: 1.3, flex: 1.15 }
    }[o.preset];

    var lines = D.order.lines.filter(function (l) { return l.desk === o.desk; }).map(function (l) {
      var zero = l.k === "count" || l.k === "dead";
      var f = pf[l.k] !== undefined ? pf[l.k] : 1;
      var gear = o.basis === "geared" ? (l.pd ? 1.32 : 1.04) : 1;
      var oh = Math.max(0, l.oh);
      var need = l.r * horizon * f * gear - oh;
      var qty = zero ? 0 : Math.max(0, Math.ceil(need / l.cs) * l.cs);
      var floorHeld = false;
      if (l.k === "kvi" && qty < l.fl) { qty = l.fl; floorHeld = true; }
      return {
        l: l, qty: qty, before: qty, zero: zero, floorHeld: floorHeld, trimmed: false,
        gear: gear > 1.05, held: l.k === "flex" && f === 0,
        cover: l.r > 0 ? oh / l.r : 999
      };
    });

    function total(ls) { var t = 0; ls.forEach(function (r) { t += r.qty * r.l.c; }); return t; }
    var t = total(lines), fitApplied = false;
    if (o.fit === "on" && t > desk.budget) {
      var prot = 0, flexV = 0;
      lines.forEach(function (r) { if (r.l.k === "kvi") prot += r.qty * r.l.c; else flexV += r.qty * r.l.c; });
      var room = Math.max(0, desk.budget - prot);
      if (flexV > room) {
        var k = flexV > 0 ? room / flexV : 0;
        lines.forEach(function (r) {
          if (r.l.k === "kvi" || r.qty === 0) return;
          var q = Math.floor((r.qty * k) / r.l.cs) * r.l.cs;
          if (q < r.qty) { r.trimmed = true; r.qty = Math.max(0, q); fitApplied = true; }
        });
        t = total(lines);
      }
    }

    var units = 0, zeros = 0, filled = 0;
    lines.forEach(function (r) { units += r.qty; if (r.qty === 0) zeros++; else filled++; });
    return {
      desk: desk, lines: lines, total: t, units: units, zeros: zeros, filled: filled,
      gap: gap, horizon: horizon, fitApplied: fitApplied
    };
  }

  function modePill(r) {
    var l = r.l;
    if (l.k === "count") return ["amber", "Count first"];
    if (l.k === "dead") return ["slate", "No order"];
    if (r.qty === 0 && r.held) return ["amber", "Held back"];
    if (r.qty === 0) return ["slate", "Covered"];
    if (l.k === "kvi") return ["green", r.floorHeld ? "Floor held" : "Protected"];
    if (r.trimmed) return ["amber", "Budget scaled"];
    if (r.gear) return ["green", "Window build"];
    if (l.k === "flex") return ["green", "Flexible refill"];
    return ["green", "Refill"];
  }
  function lineWhy(r) {
    var s = r.l.story, add = [];
    if (r.held) add.push("This preset stands the line still for one delivery, and it comes back on the standard preset.");
    if (r.gear && r.qty > 0) add.push("The geared basis stepped it up for the wage window rather than after it.");
    if (r.trimmed) add.push("The budget fit trimmed this line from " + int(r.before) + " to " + int(r.qty) + " so the protected lines kept their floors.");
    if (r.floorHeld) add.push("The floor decided this quantity, not the rate.");
    if (!r.zero && r.qty === 0 && !r.held) add.push("There is enough on hand to reach the following delivery, so nothing is ordered and nothing is missing.");
    return s + (add.length ? " " + add.join(" ") : "");
  }

  function viewOrders() {
    var o = S.ord;
    var desks = D.order.desks.filter(function (d) { return o.store === "all" || d.st === o.store; });
    if (!desks.some(function (d) { return d.v === o.desk; })) { o.desk = desks[0].v; }
    var R = computeOrder(), desk = R.desk;
    var used = desk.budget ? (R.total / desk.budget) * 100 : 0;
    var nextDates = D.order.dates.filter(function (d) { return Date.parse(d.v) > Date.parse(o.del); });
    if (!nextDates.length) { nextDates = [D.order.dates[D.order.dates.length - 1]]; }
    if (!nextDates.some(function (d) { return d.v === o.nxt; })) { o.nxt = nextDates[0].v; R = computeOrder(); }

    var rail = '<div class="dx-rail">' +
      chips("Stores", D.meta.stores, o.store, "ord.store") +
      chips("Desk", desks.map(function (d) { return { v: d.v, t: d.t }; }), o.desk, "ord.desk") +
      "</div>" +
      '<div class="dx-rail">' +
      selectField("Delivery date", D.order.dates, o.del, "ord.del") +
      selectField("Following delivery", nextDates, o.nxt, "ord.nxt") +
      seg("Preset", D.order.presets, o.preset, "ord.preset") +
      seg("Order basis", D.order.bases, o.basis, "ord.basis") +
      seg("Fit to budget", [{ v: "on", t: "Fit on" }, { v: "off", t: "Fit off" }], o.fit, "ord.fit") +
      '<button type="button" class="btn" data-act="ord.gen">Generate order</button>' +
      "</div>";

    var head = '<div class="dx-cols" style="margin-bottom:16px"><div class="dx-card">' +
      '<div class="dx-total' + (o.stamp ? " dx-flash" : "") + '"><small>Order value, this desk</small>' + money(R.total) + "</div>" +
      '<div class="dx-budget' + (R.total > desk.budget ? " over" : "") + '"><div class="bl"><span>' + money(R.total) + " of " + money(desk.budget) + " route budget</span><span>" + d1(used) + "% used</span></div>" +
      bar(R.total / desk.budget, R.total > desk.budget) + "</div>" +
      '<p class="dx-ctx" style="margin:12px 0 0">' + R.filled + " lines ordered &middot; " + R.zeros + " at zero by decision &middot; " + int(R.units) + " units &middot; " + esc(desk.t) + "</p>" +
      '<p class="dx-basis"><b>Basis for this delivery:</b> demonstrated demand, projected from ' + dateLabel(o.del) + " to the following delivery on " + dateLabel(o.nxt) +
      " &middot; preset <b>" + esc(presetLabel()) + "</b> &middot; basis <b>" + (o.basis === "geared" ? "geared to the wage window" : "normal week") + "</b> &middot; budget fit <b>" +
      (o.fit === "on" ? (R.fitApplied ? "on, and it bit" : "on, nothing to trim") : "off") + "</b></p>" +
      "</div>" + scenarioPanel(R) + "</div>";

    var headHTML = '<div class="dx-head"><span>Product</span><span class="r">Rate</span><span class="r">On hand</span><span class="r">Qty</span><span class="r">Value</span><span class="r">Mode</span></div>';
    var rowsHTML = R.lines.map(function (r) {
      var p = modePill(r);
      var cls = r.zero ? "warn" : r.qty === 0 ? "" : r.l.k === "kvi" ? "good" : "";
      return '<div class="dx-row ' + cls + '">' +
        '<span class="dx-id"><b>' + esc(r.l.n) + '</b><span class="dx-sub">' + esc(r.l.d) + " &middot; " + esc(r.l.pk) + "</span></span>" +
        '<span class="dx-figs">' +
        '<span class="dx-fig mut"><i>Rate</i><b>' + d1(r.l.r) + " u/d</b></span>" +
        '<span class="dx-fig mut"><i>On hand</i><b>' + int(Math.max(0, r.l.oh)) + " &middot; " + (r.cover > 90 ? "long" : d1(r.cover) + "d") + "</b></span>" +
        '<span class="dx-fig acc"><i>Qty</i><b>' + int(r.qty) + "</b></span>" +
        '<span class="dx-fig"><i>Value</i><b>' + money(r.qty * r.l.c) + "</b></span></span>" +
        '<span class="dx-verdict"><span class="pill ' + p[0] + '">' + p[1] + "</span></span>" +
        reason(lineWhy(r)) + "</div>";
    }).join("");

    var tableCard = card("Generated order", R.lines.length + " lines on this route &middot; every quantity carries its reason",
      '<span class="dx-tag">At cost</span>',
      headHTML + rowsHTML +
      '<p class="dx-note">Quantities land in whole cases the supplier can actually pick. A zero with a reason beats a guess with a quantity.</p>',
      "dx-t-order");

    body.innerHTML = rail + head + tableCard + stockNowPanel(R);
    S.ord.stamp = 0;
  }

  function presetLabel() {
    var p = D.order.presets, i;
    for (i = 0; i < p.length; i++) if (p[i].v === S.ord.preset) return p[i].t;
    return "";
  }
  function scenarioPanel(R) {
    var o = S.ord, desk = R.desk;
    var protectedLines = R.lines.filter(function (r) { return r.l.k === "kvi"; }).length;
    var trimmed = R.lines.filter(function (r) { return r.trimmed; }).length;
    var held = R.lines.filter(function (r) { return r.held; }).length;
    return '<div class="dx-card"><div class="dx-card-h"><h3>Scenario overview</h3><span class="sub">what these controls did</span></div>' +
      '<div class="dx-kv">' +
      "<div><span>Route</span><b>" + esc(desk.t) + "</b></div>" +
      "<div><span>Covering</span><b>" + dateLabel(o.del) + " to " + dateLabel(o.nxt) + "</b></div>" +
      "<div><span>Preset</span><b>" + esc(presetLabel()) + "</b></div>" +
      "<div><span>Lines protected</span><b>" + protectedLines + "</b></div>" +
      "<div><span>Lines trimmed by budget</span><b>" + trimmed + "</b></div>" +
      "<div><span>Lines standing still</span><b>" + held + "</b></div>" +
      "<div><span>Units on this order</span><b>" + int(R.units) + "</b></div>" +
      "</div>" +
      '<div class="reason" style="margin-top:12px">' + D.order.presetWhy[o.preset] + " " + D.order.basisWhy[o.basis] +
      (o.fit === "on"
        ? " The budget fit takes what it needs from the flexible lines first, and it is never allowed to reach the protected ones."
        : " With the fit switched off the order asks for what the shelf needs and leaves the affordability argument to the owner.") +
      "</div></div>";
  }
  function stockNowPanel(R) {
    var byDept = {};
    R.lines.forEach(function (r) {
      var d = byDept[r.l.d] || (byDept[r.l.d] = { oh: 0, rate: 0, short: 0, n: 0 });
      d.oh += Math.max(0, r.l.oh); d.rate += r.l.r; d.n++;
      if (r.cover < 1.5) d.short++;
    });
    var keys = Object.keys(byDept).sort();
    var rows = keys.map(function (k) {
      var d = byDept[k], cover = d.rate > 0 ? d.oh / d.rate : 0;
      return '<div class="dx-dept"><span class="nm">' + esc(k) + "</span>" +
        '<span class="vl">' + d1(cover) + "d</span>" +
        '<span class="dl ' + (cover < 1.5 ? "dx-dn" : cover < 2.2 ? "dx-fl" : "dx-up") + '">' + d.n + " lines</span>" +
        '<span class="bw">' + bar(cover / 6, cover < 1.5) + "</span></div>";
    }).join("");
    var shortLines = R.lines.filter(function (r) { return r.cover < 1.5 && !r.zero; }).length;
    return card("Stock now, where the store stands",
      "days of cover on hand before this order lands",
      "", rows +
      '<div class="reason" style="margin-top:12px"><b>' + shortLines + " lines on this route run out before the following delivery</b> at the rate they are currently selling. That is what the order above is answering. Cover is measured against what each line actually sells, so a slow line with plenty on hand does not get to hide behind a department average.</div>");
  }

  /* ================================================================ router */
  var VIEWS = { rhythm: viewRhythm, movers: viewMovers, stock: viewStock, capital: viewCapital, orders: viewOrders };

  function render() {
    charts.forEach(function (c) { try { c.destroy(); } catch (e) {} });
    charts = [];
    (VIEWS[S.view] || viewRhythm)();
    body.setAttribute("aria-labelledby", "tab-" + S.view);
  }

  function setState(path, val) {
    var p = path.split(".");
    if (p.length === 1) { S[p[0]] = val; return; }
    var grp = S[p[0]], key = p[1];
    if (key === "reasons") { grp[key] = val === "1"; return; }
    grp[key] = val;
    if (p[0] === "ord" && key === "store") {
      var d = D.order.desks.filter(function (x) { return val === "all" || x.st === val; });
      if (d.length && !d.some(function (x) { return x.v === S.ord.desk; })) S.ord.desk = d[0].v;
    }
    if (p[0] === "ord" && key === "del") {
      if (Date.parse(S.ord.nxt) <= Date.parse(val)) {
        var later = D.order.dates.filter(function (x) { return Date.parse(x.v) > Date.parse(val); });
        S.ord.nxt = later.length ? later[0].v : val;
      }
    }
  }

  body.addEventListener("click", function (e) {
    var b = e.target.closest("[data-act]");
    if (!b || b.tagName === "SELECT") return;
    var act = b.getAttribute("data-act");
    if (act === "ord.gen") { S.ord.stamp = 1; render(); return; }
    var val = b.getAttribute("data-val");
    if (val === null) return;
    setState(act, val);
    render();
  });
  body.addEventListener("change", function (e) {
    var s = e.target.closest("select[data-act]");
    if (!s) return;
    setState(s.getAttribute("data-act"), s.value);
    render();
  });

  /* tabs: click plus roving arrow keys */
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".dash-tabs button"));
  function selectTab(btn, focus) {
    tabs.forEach(function (t) {
      var on = t === btn;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
    });
    S.view = btn.getAttribute("data-view");
    render();
    if (focus) btn.focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () { selectTab(t, false); });
    t.addEventListener("keydown", function (e) {
      var k = e.key, j = -1;
      if (k === "ArrowRight") j = (i + 1) % tabs.length;
      else if (k === "ArrowLeft") j = (i - 1 + tabs.length) % tabs.length;
      else if (k === "Home") j = 0;
      else if (k === "End") j = tabs.length - 1;
      if (j > -1) { e.preventDefault(); selectTab(tabs[j], true); }
    });
  });

  var themeBtn = document.getElementById("themeToggle");
  if (themeBtn) themeBtn.addEventListener("click", function () { setTimeout(render, 60); });

  render();
})();
