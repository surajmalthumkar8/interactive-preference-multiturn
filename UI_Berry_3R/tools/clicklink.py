r"""Click a named link or button after re-reading its live position.

clickchip.py only matches <button>; anchor navs are <a>. Using the wrong
matcher makes a working control look dead, which is the P27 failure.
"""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag, label = sys.argv[1], sys.argv[2]
settle = float(sys.argv[3]) if len(sys.argv) > 3 else 2.5
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
js = """(()=>{const b=[...document.querySelectorAll('a,button,[role=button]')].find(x=>
  x.getBoundingClientRect().height>0 &&
  x.innerText.replace(/\s+/g,' ').trim().toUpperCase()===%s);
  if(!b) return '';b.scrollIntoView({block:'center'});const r=b.getBoundingClientRect();
  return JSON.stringify([Math.round(r.left+r.width/2),Math.round(r.top+r.height/2)]);})()""" % json.dumps(label.upper())
pos = cdp.ev(ws, js, timeout=20)
if not pos:
    print('no link %r' % label); sys.exit(0)
time.sleep(0.6)
x, y = json.loads(pos)
raw('Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': x, 'y': y})
time.sleep(0.1)
for ev in ('mousePressed', 'mouseReleased'):
    raw('Input.dispatchMouseEvent', {'type': ev, 'x': x, 'y': y, 'button': 'left', 'clickCount': 1})
    time.sleep(0.06)
time.sleep(settle)
print('clicked %r at %d,%d' % (label, x, y))
