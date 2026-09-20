r"""Bowl one ball in Cricket Clash and swing at it during the timing window.

The shot-direction buttons only mount while the delivery is in flight, so a
probe that samples before or after the window sees nothing and would wrongly
report them missing (REVIEW_LESSONS.md P23). This clicks BOWL, then polls for
a direction button and clicks it the moment one appears.
"""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag = sys.argv[1]
shot = sys.argv[2] if len(sys.argv) > 2 else 'STRAIGHT'
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)

def click(x, y):
    raw('Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': x, 'y': y})
    for ev in ('mousePressed', 'mouseReleased'):
        raw('Input.dispatchMouseEvent', {'type': ev, 'x': x, 'y': y, 'button': 'left', 'clickCount': 1})
        time.sleep(0.05)

FIND = """(()=>{const b=[...document.querySelectorAll('button')].find(x=>
  x.innerText.replace(/\s+/g,' ').trim().toUpperCase().startsWith('%s')&&x.getBoundingClientRect().height>0);
  if(!b) return '';const r=b.getBoundingClientRect();
  return JSON.stringify([Math.round(r.left+r.width/2),Math.round(r.top+r.height/2)]);})()"""

pos = cdp.ev(ws, FIND % 'BOWL NEXT BALL', timeout=20)
if not pos:
    print('no BOWL button'); sys.exit(0)
x, y = json.loads(pos)
click(x, y)

hit = None
for _ in range(40):
    time.sleep(0.12)
    p = cdp.ev(ws, FIND % shot, timeout=15)
    if p:
        sx, sy = json.loads(p)
        click(sx, sy)
        hit = (sx, sy)
        break
time.sleep(2.2)
print('bowled; shot %s at %s' % (shot, hit))
