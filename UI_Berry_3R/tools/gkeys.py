r"""Hold movement keys in a canvas game, then report. Real key events via CDP.

Usage: python gkeys.py <frag> <keys> <hold_seconds>
  keys e.g. "w" or "wd" (held together)
"""
import sys, json, time, urllib.request, websocket
import cdp, mouse

frag, keys = sys.argv[1], sys.argv[2]
hold = float(sys.argv[3]) if len(sys.argv) > 3 else 1.5
SPEC = {'w': (87, 'KeyW'), 'a': (65, 'KeyA'), 's': (83, 'KeyS'), 'd': (68, 'KeyD'),
        'e': (69, 'KeyE'), 'm': (77, 'KeyM'), 'f': (70, 'KeyF'), 'r': (82, 'KeyR'),
        '1': (49, 'Digit1'), '2': (50, 'Digit2'), '3': (51, 'Digit3'), '4': (52, 'Digit4')}
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
t = next(v for v in tabs if frag in v.get('url', ''))
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
for k in keys:
    c, code = SPEC[k]
    raw('Input.dispatchKeyEvent', {'type': 'keyDown', 'windowsVirtualKeyCode': c,
                                   'code': code, 'key': k, 'text': k})
time.sleep(hold)
for k in keys:
    c, code = SPEC[k]
    raw('Input.dispatchKeyEvent', {'type': 'keyUp', 'windowsVirtualKeyCode': c, 'code': code, 'key': k})
time.sleep(0.5)
print('held %s for %ss' % (keys, hold))
