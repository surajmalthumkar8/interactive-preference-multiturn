import cdp, time, json

def attempt():
    try:
        ws = cdp.conn('linkedin.com/ai-trainer')
    except Exception as e:
        return ('ERR', str(e)[:70])
    try:
        cdp.ev(ws, '(()=>{window.__claimLog=[];return 1;})()', timeout=20)
        cdp.ev(ws, open('hook.js').read(), timeout=20)
        cdp.ev(ws, open('claim.js').read(), timeout=25)
        time.sleep(4)
        log = cdp.ev(ws, 'JSON.stringify(window.__claimLog||[])', timeout=20)
        if not log or log == '[]':
            return ('NONE', 'no request')
        e = json.loads(log)[-1]
        return (str(e.get('s')), str(e.get('b'))[:150])
    except Exception as ex:
        return ('ERR', str(ex)[:80])
    finally:
        try: ws.close()
        except Exception: pass

for i in range(200):
    s, b = attempt()
    if s == '200':
        print('CLAIMED ' + b, flush=True)
        break
    if s not in ('404',):
        print('STATUS %s :: %s' % (s, b), flush=True)
    time.sleep(20)
else:
    print('POOL STILL EMPTY after 200 attempts', flush=True)
