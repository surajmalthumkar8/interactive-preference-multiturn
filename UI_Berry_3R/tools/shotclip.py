r"""Screenshot only the real viewport rectangle.

Page.captureScreenshot returns the full backing surface, which on a page whose
canvas has a larger backing store than the CSS viewport leaves dark bands at the
edges that no user ever sees. Reporting one of those as a visual defect would be
a false positive, so this clips to window.innerWidth/innerHeight.

Usage: python shotclip.py <frag> <name> [wait]
"""
import sys, json, time, base64, urllib.request, websocket
import cdp, mouse

frag, name = sys.argv[1], sys.argv[2]
wait = float(sys.argv[3]) if len(sys.argv) > 3 else 0
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(x for x in tabs if frag in x.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
if wait:
    time.sleep(wait)
w = cdp.ev(ws, 'window.innerWidth', timeout=20)
h = cdp.ev(ws, 'window.innerHeight', timeout=20)
r = raw('Page.captureScreenshot', {'format': 'png',
        'clip': {'x': 0, 'y': 0, 'width': w, 'height': h, 'scale': 1}})
out = r'C:\Users\Suraj\.claude\playwright-output\%s.png' % name
open(out, 'wb').write(base64.b64decode(r['result']['data']))
print('saved %s  (%sx%s)' % (out, w, h))
