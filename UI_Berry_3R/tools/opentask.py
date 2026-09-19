"""Open a Feather task page with WebGL + rAF disabled so heavy candidates cannot wedge it.
Usage: python opentask.py <feather-task-uuid>"""
import cdp, mouse, time, json, sys, urllib.request, urllib.parse, websocket

HOOK = """(()=>{
  try{ HTMLCanvasElement.prototype.getContext = function(){ return null; }; }catch(e){}
  try{ window.requestAnimationFrame = function(){ return 0; }; }catch(e){}
  window.__noglInstalled = true;
})()"""

def open_task(uuid, wait=35):
    url = 'https://msft.feather-prod.azure.com/tasks/' + uuid
    # close any existing copy first
    tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
    for t in tabs:
        if uuid in t.get('url', ''):
            urllib.request.urlopen('http://127.0.0.1:9222/json/close/' + t['id'], timeout=8).read()
    time.sleep(2)
    u = 'http://127.0.0.1:9222/json/new?' + urllib.parse.quote('about:blank', safe=':/?&=#%')
    t = json.loads(urllib.request.urlopen(urllib.request.Request(u, method='PUT'), timeout=20).read().decode())
    ws = websocket.create_connection(t['webSocketDebuggerUrl'], timeout=60, suppress_origin=True)
    raw = mouse.mkraw(ws)
    raw('Page.enable', {})
    raw('Page.addScriptToEvaluateOnNewDocument', {'source': HOOK})
    raw('Page.navigate', {'url': url})
    time.sleep(wait)
    cdp.p('READY: ' + str(cdp.ev(ws, 'document.readyState', timeout=30)))
    cdp.p('nogl: ' + str(cdp.ev(ws, '!!window.__noglInstalled', timeout=20)))
    return ws

if __name__ == '__main__':
    ws = open_task(sys.argv[1])
    cdp.p(cdp.ev(ws, 'document.body.innerText.slice(0,900)', timeout=25))
