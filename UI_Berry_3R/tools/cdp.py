import json, urllib.request, websocket, sys

def conn(match):
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
    t = [x for x in tabs if match in x.get('url','') and x.get('type')=='page']
    if not t:
        raise RuntimeError('no tab matching ' + match)
    return websocket.create_connection(t[0]['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)

_id = [0]
def ev(ws, expr, awaitp=True, timeout=60):
    _id[0] += 1
    mid = _id[0]
    ws.send(json.dumps({'id': mid, 'method': 'Runtime.evaluate',
        'params': {'expression': expr, 'returnByValue': True, 'awaitPromise': awaitp,
                   'userGesture': True}}))
    ws.settimeout(timeout)
    while True:
        m = json.loads(ws.recv())
        if m.get('id') == mid:
            r = m.get('result', {})
            if 'exceptionDetails' in r:
                return {'ERROR': str(r['exceptionDetails'])[:600]}
            return r.get('result', {}).get('value')

def newtab(url):
    u = 'http://127.0.0.1:9222/json/new?' + urllib.parse.quote(url, safe=':/?&=#%')
    req = urllib.request.Request(u, method='PUT')
    return json.loads(urllib.request.urlopen(req, timeout=15).read().decode())

def p(s):
    import sys
    sys.stdout.buffer.write((str(s)+"\n").encode('utf-8','replace'))
    sys.stdout.flush()
