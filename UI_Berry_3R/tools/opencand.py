r"""Open a candidate iframe origin in its own tab, full canvas/WebGL intact.

The task page runs with the nogl hook (opentask.py) so a heavy candidate
cannot wedge the renderer. The candidates themselves still have to be
judged with real canvas, so they get their own tabs without the hook.

Usage: python opencand.py <candidate-url> [wait]
"""
import sys, json, time, urllib.request, urllib.parse, websocket
import cdp, mouse

url = sys.argv[1]
wait = int(sys.argv[2]) if len(sys.argv) > 2 else 25

tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
for t in tabs:
    if url.rstrip('/') in t.get('url', '').rstrip('/'):
        urllib.request.urlopen('http://127.0.0.1:9222/json/close/' + t['id'], timeout=8).read()
time.sleep(1.5)

u = 'http://127.0.0.1:9222/json/new?' + urllib.parse.quote('about:blank', safe=':/?&=#%')
t = json.loads(urllib.request.urlopen(urllib.request.Request(u, method='PUT'), timeout=20).read().decode())
ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
raw = mouse.mkraw(ws)
raw('Page.enable', {})
raw('Page.navigate', {'url': url})
time.sleep(wait)
cdp.p('READY: ' + str(cdp.ev(ws, 'document.readyState', timeout=30)))
cdp.p('TITLE: ' + str(cdp.ev(ws, 'document.title', timeout=20)))
