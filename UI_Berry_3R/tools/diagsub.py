"""Submit and print the updateTaskStatus response body (LINKEDIN_PLATFORM.md 21).
Usage: python diagsub.py <task-uuid>"""
import sys, json, time, urllib.request, websocket
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp, mouse
uuid=sys.argv[1]
tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
t=[x for x in tabs if uuid[:8] in x.get('url','')][0]
urllib.request.urlopen('http://127.0.0.1:9222/json/activate/'+t['id'],timeout=10).read()
ws=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=120,suppress_origin=True)
raw=mouse.mkraw(ws); raw('Page.enable',{}); raw('Network.enable',{}); raw('Page.bringToFront',{}); time.sleep(2)
cdp.ev(ws,"(()=>{window.scrollTo(0,0);return 1;})()",timeout=20); time.sleep(1)

st=cdp.ev(ws,"(()=>{const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Submit Task');return b?'open':'closed';})()",timeout=25)
if st!='open':
    cdp.ev(ws,"""(()=>{const b=[...document.querySelectorAll('button')].find(x=>/In progress/i.test(x.innerText));
      const pk=Object.keys(b).find(k=>k.startsWith('__reactProps'));
      b[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:b,target:b,type:'click'});return 1;})()""",timeout=25)
    time.sleep(3)
    cdp.ev(ws,"""(()=>{const it=[...document.querySelectorAll('[role=menuitem],li.MuiMenuItem-root,.MuiMenu-list li')]
      .find(e=>e.innerText.trim()==='Mark as complete');
      const pk=Object.keys(it).find(k=>k.startsWith('__reactProps'));
      it[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:it,target:it,type:'click'});return 1;})()""",timeout=25)
    time.sleep(4)

r=cdp.ev(ws,"""(()=>{const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Submit Task');
  if(!b) return null; const q=b.getBoundingClientRect();
  return JSON.stringify({x:Math.round(q.x+q.width/2),y:Math.round(q.y+q.height/2)});})()""",timeout=25)
if not r or isinstance(r,dict): cdp.p('NO CONFIRM BUTTON'); raise SystemExit(1)
q=json.loads(r)
ws.settimeout(1.0)
try:
    while True: ws.recv()
except Exception: pass
mouse.click_at(ws,q['x'],q['y'],settle=1.0)
rid=None; t0=time.time(); ws.settimeout(2.0)
while time.time()-t0<16:
    try: m=json.loads(ws.recv())
    except Exception: continue
    if m.get('method')=='Network.requestWillBeSent' and 'UpdateTaskStatus' in str(m['params']['request'].get('postData','')):
        rid=m['params']['requestId']
    if m.get('method')=='Network.loadingFinished' and rid and m['params']['requestId']==rid:
        time.sleep(0.4)
        body=raw('Network.getResponseBody',{'requestId':rid}).get('result',{}).get('body','')
        cdp.p('BODY: '+str(body)[:700]); break
if not rid: cdp.p('no UpdateTaskStatus fired')
