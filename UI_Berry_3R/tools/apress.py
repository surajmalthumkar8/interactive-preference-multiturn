r"""Send a real key press to a tab by URL fragment (CDP Input.dispatchKeyEvent)."""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag = sys.argv[1]
key = sys.argv[2] if len(sys.argv) > 2 else 'Space'
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(x for x in tabs if frag in x.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
raw('Input.dispatchMouseEvent', {'type': 'mousePressed', 'x': 700, 'y': 500, 'button': 'left', 'clickCount': 1})
raw('Input.dispatchMouseEvent', {'type': 'mouseReleased', 'x': 700, 'y': 500, 'button': 'left', 'clickCount': 1})
time.sleep(0.4)
spec = {'Space': (32, ' ', 'Space'), 'ArrowUp': (38, '', 'ArrowUp'), 'ArrowDown': (40, '', 'ArrowDown')}
code, txt, dom = spec.get(key, (32, ' ', 'Space'))
raw('Input.dispatchKeyEvent', {'type': 'keyDown', 'windowsVirtualKeyCode': code, 'code': dom, 'key': ' ' if code == 32 else dom, 'text': txt})
time.sleep(0.05)
raw('Input.dispatchKeyEvent', {'type': 'keyUp', 'windowsVirtualKeyCode': code, 'code': dom, 'key': ' ' if code == 32 else dom})
print('pressed ' + key)
