r"""Real mouse click at page coordinates, by tab URL fragment.

Canvas games and pointer-event UIs ignore a synthetic element.click().
Calling something broken on the strength of a synthetic click is the
false-negative pattern in REVIEW_LESSONS.md P21, so negative claims about
a control have to go through a real Input.dispatchMouseEvent first.

Usage: python mclick.py <url-fragment> <x> <y> [settle_seconds]
"""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag, x, y = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
settle = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
raw('Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': x, 'y': y})
time.sleep(0.12)
for ev in ('mousePressed', 'mouseReleased'):
    raw('Input.dispatchMouseEvent', {'type': ev, 'x': x, 'y': y, 'button': 'left', 'clickCount': 1})
    time.sleep(0.06)
time.sleep(settle)
print('clicked %d,%d' % (x, y))
