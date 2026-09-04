/* Adoption curve. Data is injected by tools/build_site.py as window.ADOPTION. */
(function () {
  "use strict";

  var DATA = window.ADOPTION || [];
  if (DATA.length < 2) { return; }

  // Slot order is the validated CVD-safe order: blue, orange, aqua, yellow.
  var SERIES = [
    { key: "total",      name: "Total tracked", css: "--s-total" },
    { key: "working",    name: "Working on it", css: "--s-working" },
    { key: "supporting", name: "Supporting",    css: "--s-supporting" },
    { key: "dont",       name: "Don’t",    css: "--s-dont" }
  ];

  var W = 960, H = 452;
  var L = 62, R = 786, T = 26, B = 396;
  var D0 = DATA[0].day, D1 = DATA[DATA.length - 1].day;

  var peak = DATA.reduce(function (m, d) { return Math.max(m, d.total); }, 0);
  var step = peak > 400 ? 100 : (peak > 200 ? 50 : 40);
  var Y_MAX = Math.ceil((peak * 1.06) / step) * step;
  var Y_TICKS = [];
  for (var t = 0; t <= Y_MAX; t += step) { Y_TICKS.push(t); }

  function x(day) { return L + (day - D0) / (D1 - D0) * (R - L); }
  function y(v) { return B - (v / Y_MAX) * (B - T); }
  function col(s) { return "var(" + s.css + ")"; }

  var NS = "http://www.w3.org/2000/svg";
  function el(name, attrs, text) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) { if (attrs[k] !== null) { n.setAttribute(k, attrs[k]); } }
    if (text !== undefined) { n.appendChild(document.createTextNode(text)); }
    return n;
  }

  var svg = document.getElementById("plot");

  Y_TICKS.forEach(function (v) {
    var yy = y(v);
    svg.appendChild(el("line", { x1: L, x2: R, y1: yy, y2: yy, "class": v === 0 ? "axis-line" : "grid-line" }));
    svg.appendChild(el("text", { x: L - 12, y: yy + 4, "class": "tick", "text-anchor": "end" }, String(v)));
  });
  svg.appendChild(el("text", { x: 2, y: T - 10, "class": "axis-title", "text-anchor": "start" }, "Projects"));

  DATA.forEach(function (d) {
    var xx = x(d.day);
    svg.appendChild(el("line", { x1: xx, x2: xx, y1: B, y2: B + 6, "class": "axis-line" }));
    svg.appendChild(el("text", { x: xx, y: B + 22, "class": "tick", "text-anchor": "middle" }, "+" + d.day));
    svg.appendChild(el("text", { x: xx, y: B + 36, "class": "tick-date", "text-anchor": "middle" }, d.date.slice(5)));
  });
  svg.appendChild(el("text", { x: (L + R) / 2, y: H - 6, "class": "axis-title", "text-anchor": "middle" },
    "Days after RFC publication"));

  var cross = el("line", { x1: 0, x2: 0, y1: T, y2: B, "class": "crosshair" });
  svg.appendChild(cross);

  SERIES.forEach(function (s) {
    var dstr = DATA.map(function (d, i) {
      return (i ? "L" : "M") + x(d.day).toFixed(1) + " " + y(d[s.key]).toFixed(1);
    }).join(" ");
    svg.appendChild(el("path", { d: dstr, "class": "series-line", style: "stroke:" + col(s) }));
  });

  SERIES.forEach(function (s) {
    DATA.forEach(function (d) {
      svg.appendChild(el("circle", {
        cx: x(d.day).toFixed(1), cy: y(d[s.key]).toFixed(1), r: 4,
        "class": "marker", style: "fill:" + col(s)
      }));
    });
  });

  /* direct end labels — mandatory at four series */
  var last = DATA[DATA.length - 1];
  var placed = SERIES.map(function (s) {
    return { s: s, v: last[s.key], y: y(last[s.key]) };
  }).sort(function (a, b) { return a.y - b.y; });
  for (var i = 1; i < placed.length; i++) {
    if (placed[i].y - placed[i - 1].y < 36) { placed[i].y = placed[i - 1].y + 36; }
  }
  placed.forEach(function (p) {
    var lx = R + 16;
    svg.appendChild(el("line", {
      x1: R + 5, x2: lx - 5, y1: y(p.v), y2: p.y - 4,
      style: "stroke:" + col(p.s), "stroke-width": 1, opacity: 0.45
    }));
    svg.appendChild(el("text", { x: lx, y: p.y - 4, "class": "end-label" }, p.s.name));
    svg.appendChild(el("text", { x: lx, y: p.y + 12, "class": "end-label-sub" }, String(p.v) + " projects"));
  });

  /* legend */
  var legend = document.getElementById("legend");
  SERIES.forEach(function (s) {
    var item = document.createElement("span");
    item.className = "legend-item";
    var key = document.createElement("span");
    key.className = "legend-key";
    key.style.background = col(s);
    var label = document.createElement("span");
    label.textContent = s.name;
    item.appendChild(key);
    item.appendChild(label);
    legend.appendChild(item);
  });

  /* table view */
  var tbody = document.getElementById("chart-tbody");
  DATA.forEach(function (d) {
    var tr = document.createElement("tr");
    [d.date, "+" + d.day, d.total, d.working, d.supporting, d.dont, d.declined, d.none]
      .forEach(function (c, idx) {
        var td = document.createElement("td");
        if (idx === 1) { td.className = "day"; }
        td.textContent = String(c);
        tr.appendChild(td);
      });
    tbody.appendChild(tr);
  });

  /* hover: crosshair snaps to the nearest snapshot, one tooltip lists every series */
  var tip = document.getElementById("tip");
  var shell = document.getElementById("shell");
  var hit = el("rect", { x: L - 24, y: T, width: (R - L) + 48, height: B - T, "class": "hit", tabindex: "0" });
  svg.appendChild(hit);

  function nearest(px) {
    var best = 0, bd = Infinity;
    DATA.forEach(function (d, i) {
      var dist = Math.abs(x(d.day) - px);
      if (dist < bd) { bd = dist; best = i; }
    });
    return best;
  }

  function render(idx) {
    var d = DATA[idx];
    tip.textContent = "";

    var head = document.createElement("div");
    head.className = "tip-head";
    head.textContent = "Day +" + d.day + " · " + d.date;
    tip.appendChild(head);

    SERIES.forEach(function (s) {
      var row = document.createElement("div");
      row.className = "tip-row";
      var k = document.createElement("span");
      k.className = "tip-key";
      k.style.background = col(s);
      var n = document.createElement("span");
      n.className = "tip-name";
      n.textContent = s.name;
      var v = document.createElement("span");
      v.className = "tip-val";
      v.textContent = String(d[s.key]);
      row.appendChild(k);
      row.appendChild(n);
      row.appendChild(v);
      tip.appendChild(row);
    });

    var foot = document.createElement("div");
    foot.className = "tip-foot";
    foot.textContent = "Don’t = " + d.declined + " declined + " + d.none + " no signal";
    tip.appendChild(foot);

    var rect = svg.getBoundingClientRect();
    var scale = rect.width / W;
    var px = x(d.day) * scale;
    cross.setAttribute("x1", x(d.day));
    cross.setAttribute("x2", x(d.day));
    cross.style.opacity = "1";
    tip.classList.add("on");

    var tw = tip.offsetWidth;
    var left = px + 18;
    if (left + tw > shell.clientWidth) { left = px - tw - 18; }
    if (left < 0) { left = 0; }
    tip.style.left = left + "px";
    tip.style.top = (T * scale + 8) + "px";
  }

  function hide() {
    tip.classList.remove("on");
    cross.style.opacity = "0";
  }

  var current = -1;
  hit.addEventListener("pointermove", function (ev) {
    var rect = svg.getBoundingClientRect();
    var px = (ev.clientX - rect.left) / (rect.width / W);
    current = nearest(px);
    render(current);
  });
  hit.addEventListener("pointerleave", hide);
  hit.addEventListener("focus", function () { current = DATA.length - 1; render(current); });
  hit.addEventListener("blur", hide);
  hit.addEventListener("keydown", function (ev) {
    if (ev.key === "ArrowLeft" || ev.key === "ArrowRight") {
      ev.preventDefault();
      if (current < 0) { current = DATA.length - 1; }
      current = Math.max(0, Math.min(DATA.length - 1, current + (ev.key === "ArrowRight" ? 1 : -1)));
      render(current);
    }
  });
})();
