// Uritorco - one-shot layout and visual audit for a candidate app.
//
// Paste the whole function as the argument to a single browser_evaluate call, with the
// candidate app open in its own tab at the width being tested. It replaces roughly a dozen
// separate round trips with one.
//
// Run it twice per app: once at 1440x900 (desktop) and once at 390x844 (mobile).
//
// Everything it returns is a MEASUREMENT, not a finding. A number here is a hypothesis to
// confirm with a viewport screenshot before it goes anywhere near a rubric field.

() => {
  const vw = window.innerWidth;
  const de = document.documentElement;

  // --- page level overflow -------------------------------------------------
  // The one that a full-page screenshot will hide from you, because a full-page
  // capture widens the canvas to fit the content.
  const pageOverflow = {
    scrollW: de.scrollWidth,
    innerW: vw,
    overflows: de.scrollWidth > vw + 1,
    overflowBy: Math.max(0, de.scrollWidth - vw),
  };

  // --- what is actually off screen ----------------------------------------
  const offscreen = [];
  document.querySelectorAll('*').forEach((el) => {
    const r = el.getBoundingClientRect();
    if (r.width > 0 && r.right > vw + 1) {
      offscreen.push({
        tag: el.tagName,
        id: el.id || '',
        cls: (el.className || '').toString().slice(0, 40),
        right: Math.round(r.right),
      });
    }
  });

  // --- table columns: which headers can a user not see? -------------------
  const table = document.querySelector('table');
  let columns = null;
  if (table) {
    const heads = [...table.querySelectorAll('thead th')].map((th) => {
      const r = th.getBoundingClientRect();
      return {
        text: th.innerText.trim(),
        visible: r.right <= vw,
        partial: r.left < vw && r.right > vw,
      };
    });
    const wrapper = table.parentElement;
    const ws = wrapper ? getComputedStyle(wrapper) : null;
    const contained = wrapper
      ? ws.overflowX === 'auto' || ws.overflowX === 'scroll'
      : false;
    columns = {
      count: heads.length,
      headers: heads.map((h) => h.text),
      // Columns past the viewport edge. This is ONLY a defect when the page itself
      // overflows. When the table sits in its own scroller the user simply scrolls the
      // strip, which is the correct pattern, so the list is reported as reachable
      // rather than cut off. Read `unreachable`, not `pastViewportEdge`.
      pastViewportEdge: heads.filter((h) => !h.visible).map((h) => h.text),
      unreachable:
        !contained && pageOverflow.overflows
          ? heads.filter((h) => !h.visible).map((h) => h.text)
          : [],
      // A wide table is only a defect when the PAGE overflows. Contained in its own
      // scroller is the correct pattern and must not be written up as a fault.
      containedInOwnScroller: contained,
      wrapperScrolls: wrapper ? wrapper.scrollWidth > wrapper.clientWidth : null,
      theadHidden: table.querySelector('thead')
        ? getComputedStyle(table.querySelector('thead')).display === 'none'
        : null, // true means a mobile card layout is in effect
      bodyRowCount: table.querySelectorAll('tbody tr').length,
      emptyStateText: table.querySelector('tbody')
        ? table.querySelector('tbody').innerText.trim().slice(0, 80)
        : null,
    };
  }

  // --- form rows that refuse to stack -------------------------------------
  const formRows = [...document.querySelectorAll('.form-row, .form-grid, form > div')]
    .slice(0, 6)
    .map((r) => {
      const cs = getComputedStyle(r);
      const bb = r.getBoundingClientRect();
      return {
        cls: (r.className || '').toString().slice(0, 30),
        display: cs.display,
        flexWrap: cs.flexWrap,
        gridCols: cs.gridTemplateColumns,
        overflowsBy: Math.round(Math.max(0, bb.right - vw)),
      };
    });

  // --- inline elements whose background breaks across lines ---------------
  // display:inline on a pill means the background paints once PER LINE BOX, so a
  // two-word label that wraps renders as two separate coloured blocks.
  const pills = [...document.querySelectorAll('.pill, .badge, .tag, .chip')].map((p) => {
    const rects = [...p.getClientRects()];
    return {
      text: p.innerText.trim().slice(0, 24),
      display: getComputedStyle(p).display,
      fragments: rects.length,
      broken: rects.length > 1,
    };
  });

  // --- currency and number formatting -------------------------------------
  const cells = [...document.querySelectorAll('td')].map((td) => td.innerText.trim());
  const moneyish = cells.filter((c) => /^[\d,.]+$/.test(c) && c.length > 2).slice(0, 5);

  // --- which breakpoints are actually in effect ---------------------------
  const media = [];
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule.type === CSSRule.MEDIA_RULE) {
          media.push({
            query: rule.conditionText,
            matches: window.matchMedia(rule.conditionText).matches,
          });
        }
      }
    } catch (e) {
      /* cross origin sheet, skip */
    }
  }

  return {
    width: vw,
    pageOverflow,
    offscreenCount: offscreen.length,
    offscreenTop: offscreen.slice(0, 6),
    columns,
    formRows,
    pills,
    unformattedNumbers: moneyish,
    mediaQueries: media,
  };
}
