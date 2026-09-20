r"""Click a named chip/button after re-reading its live position.

Filtering a list reflows the page, so coordinates captured before a click are
stale by the next one. Reading the position immediately before each click is
what stops a stale-coordinate miss being misread as a dead control (P21).

Usage: python clickchip.py <frag> "<label>" [settle]
"""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag, label = sys.argv[1], sys.argv[2]
settle = float(sys.argv[3]) if len(sys.argv) > 3 else 2.5
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
js = """(()=>{const b=[...document.querySelectorAll('button')].find(x=>
  x.getBoundingClientRect().height>0 &&
  x.innerText.replace(/\s+/g,' ').trim().toUpperCase().startsWith(%s));
  if(!b) return '';const r=b.getBoundingClientRect();
  return JSON.stringify([Math.round(r.left+r.width/2),Math.round(r.top+r.height/2)]);})()""" % json.dumps(label.upper())
pos = cdp.ev(ws, js, timeout=20)
if not pos:
    print('no chip %r' % label); sys.exit(0)
x, y = json.loads(pos)
raw('Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': x, 'y': y})
time.sleep(0.1)
for ev in ('mousePressed', 'mouseReleased'):
    raw('Input.dispatchMouseEvent', {'type': ev, 'x': x, 'y': y, 'button': 'left', 'clickCount': 1})
    time.sleep(0.06)
time.sleep(settle)
print('clicked %r at %d,%d' % (label, x, y))
