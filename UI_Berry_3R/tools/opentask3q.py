"""Open a UI Berry task end to end: read LinkedIn link, open Feather with the WebGL hook,
resolve the REAL uuid (section 20), claim it (19a), fire Start annotation, return candidate URLs.
Usage: python opentask3q.py <workitem-id>"""
import sys, json, time, re, urllib.request, urllib.parse, websocket
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp, mouse, opentask

wi = sys.argv[1]
lk = cdp.conn('linkedin.com/ai-trainer')
cdp.ev(lk, "location.href='https://www.linkedin.com/ai-trainer/tasks/%s'" % wi, awaitp=False)
time.sleep(11)
printed = cdp.ev(lk, """(()=>{const a=[...document.querySelectorAll('a')].map(x=>x.href)
   .filter(h=>h.indexOf('feather')>-1); return a[0]||null;})()""", timeout=30)
cdp.p('printed link: '+str(printed))
puuid = re.search(r'/tasks/([0-9a-f-]{36})', printed).group(1)

ws = opentask.open_task(puuid, wait=32)

# section 20: the tab may have resolved to a DIFFERENT uuid
real = cdp.ev(ws, "(()=>location.href)()", timeout=25)
ruuid = re.search(r'/tasks/([0-9a-f-]{36})', real).group(1)
cdp.p('printed uuid: '+puuid)
cdp.p('REAL uuid   : '+ruuid+('  (SAME)' if ruuid==puuid else '  (DIFFERENT - use this one)'))

raw = mouse.mkraw(ws); raw('Page.bringToFront',{}); time.sleep(1)
cdp.p(cdp.ev(ws, """(()=>{const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Unclaimed');
  if(!b) return 'pill not Unclaimed';
  const pk=Object.keys(b).find(k=>k.startsWith('__reactProps'));
  b[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:b,target:b,type:'click'});return 'pill opened';})()""", timeout=25))
time.sleep(3)
cdp.p(cdp.ev(ws, """(()=>{const it=[...document.querySelectorAll('[role=menuitem],li.MuiMenuItem-root,.MuiMenu-list li')]
  .find(e=>e.innerText.trim()==='Claim task'); if(!it) return 'no claim item';
  const pk=Object.keys(it).find(k=>k.startsWith('__reactProps'));
  if(pk&&it[pk].onClick){it[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:it,target:it,type:'click'});return 'claimed';}
  it.click(); return 'claimed(dom)';})()""", timeout=25))
time.sleep(7)
cdp.p('pill: '+str(cdp.ev(ws, "(()=>{const b=[...document.querySelectorAll('button')].find(x=>/Unclaim|In progress|Complete/i.test(x.innerText)); return b?b.innerText.trim():'?';})()", timeout=25)))

cdp.ev(lk, "location.href='https://www.linkedin.com/ai-trainer/tasks/%s'" % wi, awaitp=False)
time.sleep(10)
cdp.p('LinkedIn: '+str(cdp.ev(lk, """(()=>{const b=[...document.querySelectorAll('button')].find(x=>/Start annotation/i.test(x.innerText));
  if(!b) return 'no start btn';
  const k=Object.keys(b).find(x=>x.startsWith('__reactProps$'));
  b[k].onClick({preventDefault(){},stopPropagation(){},currentTarget:b,target:b,type:'click'});return 'START fired';})()""", timeout=30)))
time.sleep(5)

raw('Page.bringToFront',{}); time.sleep(1)
for lbl in ['Website A','Website B']:
    cdp.ev(ws, "(()=>{const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='%s'); if(b)b.click(); return 1;})()" % lbl, timeout=25)
    time.sleep(5)
cdp.p('iframes: '+str(cdp.ev(ws, "(()=>JSON.stringify([...document.querySelectorAll('iframe')].map(f=>f.src)))()", timeout=25)))
cdp.p('PROMPT: '+str(cdp.ev(ws, "(()=>document.body.innerText.slice(0,900))()", timeout=25)))
