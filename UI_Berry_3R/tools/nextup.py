"""Fresh-tab claim: close board tabs, open fresh, pick batch, claim, open+claim task.
Prints WI id and the canonical post-claim uuid."""
import sys,json,time,urllib.request,urllib.parse
sys.path.insert(0,r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp, mouse
T=r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools'
BATCH='solnext-jsd-s40-j128 vs exact 5p6 Aesthetics/Functionality/Overall Preference 2026-09-20'

def newtab(url):
    req='http://127.0.0.1:9222/json/new?'+urllib.parse.quote(url,safe=':/?=&')
    try: r=urllib.request.urlopen(urllib.request.Request(req,method='PUT'),timeout=15).read().decode()
    except Exception: r=urllib.request.urlopen(req,timeout=15).read().decode()
    return json.loads(r).get('id')

def closematch(frag):
    tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
    n=0
    for t in tabs:
        if t.get('type')=='page' and frag in t.get('url',''):
            try: urllib.request.urlopen('http://127.0.0.1:9222/json/close/'+t['id'],timeout=8).read(); n+=1
            except Exception: pass
    return n

closematch('ai-trainer/tasks'); closematch('.c.msft.feather-prod')
time.sleep(2)
newtab('https://www.linkedin.com/ai-trainer/tasks?projectId=1253002')
time.sleep(17)
ws=cdp.conn('projectId=1253002')
raw=mouse.mkraw(ws); raw('Page.bringToFront',{}); time.sleep(1.0)

# select batch
p=json.loads(cdp.ev(ws,"""(()=>{const b=[...document.querySelectorAll('button')]
  .find(x=>/batch/i.test(x.innerText.trim()));b.scrollIntoView({block:'center'});
  const r=b.getBoundingClientRect();
  return JSON.stringify({x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2)});})()""",timeout=30))
mouse.click_at(ws,p['x'],p['y'],settle=3.5)
q=cdp.ev(ws,"""(()=>{const e=[...document.querySelectorAll('.ant-dropdown-menu-item, .ant-dropdown li')]
  .find(x=>x.innerText.trim()===%s);
  if(!e) return 'NO ITEM'; e.scrollIntoView({block:'center'});
  const r=e.getBoundingClientRect();
  return JSON.stringify({x:Math.round(r.x+r.width/2),y:Math.round(r.y+r.height/2)});})()""" % json.dumps(BATCH),timeout=30)
if q.startswith('NO'): raise SystemExit('batch not found')
qq=json.loads(q); mouse.click_at(ws,qq['x'],qq['y'],settle=4.0)

cdp.ev(ws,open('hook20.js',encoding='utf-8').read(),timeout=25)
cdp.ev(ws,"(()=>{window.__fh2=[];return 1;})()",timeout=20)
cdp.ev(ws,open(T+r'\claim.js',encoding='utf-8').read(),timeout=30)
time.sleep(11)
resp=json.loads(cdp.ev(ws,'(()=>JSON.stringify(window.__fh2||[]))()',timeout=25))
claim=[r for r in resp if 'claimResults' in r['u']]
if not claim: raise SystemExit('no claim response: '+json.dumps(resp)[:300])
c=claim[0]
if c['s']!=200: raise SystemExit('claim HTTP %s: %s' % (c['s'], c['b'][:200]))
wi=json.loads(c['b'])['value']['approvedIds'][0]
listing=[r for r in resp if 'q=annotator' in r['u']]
link=None; title=None
for r in listing:
    m=r['b']
    i=m.find('feather-prod.azure.com/tasks/')
    if i>-1:
        link=m[i+len('feather-prod.azure.com/tasks/'):i+len('feather-prod.azure.com/tasks/')+36]
        j=m.find('title'); title=m[j:j+80] if j>-1 else ''
        break
print('WI:',wi); print('pre-claim uuid:',link); print('title:',title)
if link:
    newtab('https://msft.feather-prod.azure.com/tasks/'+link)
    time.sleep(20)
    ws2=cdp.conn(link[:8])
    print('claimgo:',cdp.ev(ws2,open('claimgo.js',encoding='utf-8').read(),timeout=60,awaitp=True))
    time.sleep(3)
    tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
    live=[t['url'].split('/tasks/')[-1] for t in tabs
          if t.get('type')=='page' and '/tasks/' in t.get('url','') and 'feather-prod' in t.get('url','')
          and 'linkedin' not in t.get('url','')]
    print('CANONICAL UUID:', live[0] if live else 'NOT FOUND')
