"""Submit a DA0518 3-question Feather task (LINKEDIN_PLATFORM.md 19b).
Mark as complete -> Confirm Submission panel (NOT a role=dialog) -> Submit Task.
Usage: python submit3q.py <task-uuid>"""
import sys, json, time, urllib.request, websocket
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp, mouse

uuid = sys.argv[1]
tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
t=[x for x in tabs if uuid[:8] in x.get('url','')][0]
urllib.request.urlopen('http://127.0.0.1:9222/json/activate/'+t['id'],timeout=10).read()
ws=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=120,suppress_origin=True)
raw=mouse.mkraw(ws); raw('Page.enable',{}); raw('Page.bringToFront',{}); time.sleep(1)

cdp.p(cdp.ev(ws,"""(()=>{
  const b=[...document.querySelectorAll('button')].find(x=>/In progress/i.test(x.innerText));
  if(!b) return 'no pill';
  const pk=Object.keys(b).find(k=>k.startsWith('__reactProps'));
  b[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:b,target:b,type:'click'});
  return 'pill opened';})()""",timeout=25))
time.sleep(3)
cdp.p(cdp.ev(ws,"""(()=>{
  const it=[...document.querySelectorAll('[role=menuitem],li.MuiMenuItem-root,.MuiMenu-list li')]
     .find(e=>e.innerText.trim()==='Mark as complete');
  if(!it) return 'no complete item';
  const pk=Object.keys(it).find(k=>k.startsWith('__reactProps'));
  if(pk&&it[pk].onClick){it[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:it,target:it,type:'click'});return 'marked';}
  it.click(); return 'marked(dom)';})()""",timeout=25))
time.sleep(4)
cdp.p(cdp.ev(ws,"""(()=>{
  const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Submit Task');
  if(!b) return 'NO CONFIRM BUTTON';
  const pk=Object.keys(b).find(k=>k.startsWith('__reactProps'));
  if(pk&&b[pk].onClick){b[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:b,target:b,type:'click'});return 'confirmed';}
  b.click(); return 'confirmed(dom)';})()""",timeout=25))
time.sleep(8)
