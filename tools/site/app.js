/* Filtering for the tracker tables. Generated site; edit tools/site/app.js. */
(function () {
  "use strict";

  var search = document.getElementById("q");
  var clearBtn = document.getElementById("q-clear");
  var resetBtn = document.getElementById("reset");
  var countEl = document.getElementById("result-count");
  var emptyEl = document.getElementById("empty");
  var tiles = Array.prototype.slice.call(document.querySelectorAll(".tile[data-status]"));
  var rows = Array.prototype.slice.call(document.querySelectorAll("tbody tr[data-status]"));
  var sections = Array.prototype.slice.call(document.querySelectorAll(".section"));

  if (!rows.length) { return; }

  // Cache the searchable text once.
  rows.forEach(function (r) {
    r.dataset.hay = (r.textContent || "").toLowerCase().replace(/\s+/g, " ");
  });

  var active = null;   // null = all statuses; otherwise a space-separated slug list
  var term = "";

  function matches(row) {
    return active.split(" ").indexOf(row.dataset.status) !== -1;
  }

  function apply() {
    var shown = 0;
    rows.forEach(function (r) {
      var okStatus = !active || matches(r);
      var okTerm = !term || r.dataset.hay.indexOf(term) !== -1;
      var show = okStatus && okTerm;
      r.classList.toggle("is-hidden", !show);
      if (show) { shown++; }
    });

    sections.forEach(function (s) {
      var secRows = s.querySelectorAll("tbody tr[data-status]");
      if (!secRows.length) {
        // prose-only sections stay put unless a filter is engaged
        s.classList.toggle("is-empty", Boolean(active) || Boolean(term));
        return;
      }
      var vis = s.querySelectorAll("tbody tr[data-status]:not(.is-hidden)").length;
      s.classList.toggle("is-empty", vis === 0);
      var badge = s.querySelector("h2 .count");
      if (badge) {
        badge.textContent = vis === secRows.length
          ? secRows.length + " rows"
          : vis + " of " + secRows.length + " rows";
      }
    });

    var filtered = Boolean(active) || Boolean(term);
    countEl.textContent = filtered
      ? shown + " of " + rows.length + " rows"
      : rows.length + " rows";
    emptyEl.classList.toggle("on", shown === 0);
    resetBtn.hidden = !filtered;

    tiles.forEach(function (t) {
      var on = t.dataset.status === "all" ? !active : t.dataset.status === active;
      t.setAttribute("aria-pressed", String(on));
    });
    clearBtn.hidden = !term;
  }

  tiles.forEach(function (t) {
    t.addEventListener("click", function () {
      var want = t.dataset.status;
      // the totals tile means "no status filter"
      active = (want === "all" || active === want) ? null : want;
      apply();
    });
  });

  search.addEventListener("input", function () {
    term = search.value.trim().toLowerCase();
    apply();
  });

  clearBtn.addEventListener("click", function () {
    search.value = "";
    term = "";
    search.focus();
    apply();
  });

  resetBtn.addEventListener("click", function () {
    search.value = "";
    term = "";
    active = null;
    apply();
  });

  // "/" focuses search, Escape clears it.
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "/" && document.activeElement !== search) {
      ev.preventDefault();
      search.focus();
    } else if (ev.key === "Escape" && document.activeElement === search) {
      search.value = "";
      term = "";
      apply();
    }
  });

  apply();
})();
