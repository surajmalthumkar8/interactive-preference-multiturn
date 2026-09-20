r"""Drag the mouse across a canvas to rotate a first-person camera.

360-degree look is usually driven by mousemove deltas, and many builds read
movementX which only exists under pointer lock. Dragging with the button held
is the closest a CDP harness can get without a real user gesture.
"""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag = sys.argv[1]
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
steps = int(sys.argv[6]) if len(sys.argv) > 6 else 12
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
raw('Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': x0, 'y': y0})
raw('Input.dispatchMouseEvent', {'type': 'mousePressed', 'x': x0, 'y': y0, 'button': 'left', 'clickCount': 1})
for i in range(1, steps + 1):
    x = round(x0 + (x1 - x0) * i / steps)
    y = round(y0 + (y1 - y0) * i / steps)
    raw('Input.dispatchMouseEvent', {'type': 'mouseMoved', 'x': x, 'y': y, 'button': 'left'})
    time.sleep(0.05)
raw('Input.dispatchMouseEvent', {'type': 'mouseReleased', 'x': x1, 'y': y1, 'button': 'left', 'clickCount': 1})
time.sleep(1.0)
print('dragged %d,%d -> %d,%d' % (x0, y0, x1, y1))
