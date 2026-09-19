import cdp, json, time

def mkraw(ws):
    def raw(method, params):
        cdp._id[0]+=1; mid=cdp._id[0]
        ws.send(json.dumps({'id':mid,'method':method,'params':params}))
        ws.settimeout(25)
        while True:
            m=json.loads(ws.recv())
            if m.get('id')==mid: return m
    return raw

def click_at(ws, x, y, settle=0.9):
    raw = mkraw(ws)
    raw('Input.dispatchMouseEvent', {'type':'mouseMoved','x':x,'y':y})
    time.sleep(0.15)
    for t in ['mousePressed','mouseReleased']:
        raw('Input.dispatchMouseEvent', {'type':t,'x':x,'y':y,'button':'left','clickCount':1})
        time.sleep(0.09)
    time.sleep(settle)

def center_of(ws, sel_js):
    r = cdp.ev(ws, sel_js)
    if not r or r=='null': return None
    return json.loads(r)
