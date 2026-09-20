r"""Screenshot a live tab by URL fragment into the playwright-output dir.

Usage: python shot.py <url-fragment> <name> [wait]
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
r = raw('Page.captureScreenshot', {'format': 'png'})
out = r'C:\Users\Suraj\.claude\playwright-output\%s.png' % name
open(out, 'wb').write(base64.b64decode(r['result']['data']))
print('saved ' + out)
