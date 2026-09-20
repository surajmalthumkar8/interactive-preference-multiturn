r"""Screenshot a sub-rectangle of the viewport, for inspecting one artifact closely."""
import sys, json, time, base64, urllib.request, websocket
import cdp, mouse
frag, name = sys.argv[1], sys.argv[2]
x, y, w, h = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
r = raw('Page.captureScreenshot', {'format': 'png',
        'clip': {'x': x, 'y': y, 'width': w, 'height': h, 'scale': scale}})
out = r'C:\Users\Suraj\.claude\playwright-output\%s.png' % name
open(out, 'wb').write(base64.b64decode(r['result']['data']))
print('saved ' + out)
