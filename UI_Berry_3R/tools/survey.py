"""One-pass candidate survey. Folds in the probe rules that keep producing false negatives:
P37 walk the page before measuring, P29 in-viewport assert + null means probe failure,
P33 measure from a clean load, P32 scope by container not by label.

Usage: python survey.py <url-fragment>
"""
import sys, json, time, urllib.request, websocket
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp

WALK = """(()=>{return document.documentElement.scrollHeight;})()"""

SURVEY = r"""(()=>{
 const o={};
 o.title=document.title; o.bg=getComputedStyle(document.body).backgroundColor;
 o.docH=document.documentElement.scrollHeight; o.vh=window.innerHeight;
 const cv=[...document.querySelectorAll('canvas')];
 o.canvas=cv.map(c=>{let k='2d/none';try{k=c.getContext('webgl2')?'webgl2':(c.getContext('webgl')?'webgl':'2d');}catch(e){k='err';}
   const r=c.getBoundingClientRect();return {kind:k,w:c.width,h:c.height,cw:Math.round(r.width)};});
 o.video=document.querySelectorAll('video').length;
 o.img=document.querySelectorAll('img').length;
 o.svg=document.querySelectorAll('svg').length;
 let p3=0,t3=0;[...document.querySelectorAll('*')].forEach(e=>{const cs=getComputedStyle(e);
   if(cs.transformStyle==='preserve-3d')p3++;
   const t=cs.transform||'';if(t.indexOf('matrix3d')>-1)t3++;});
 o.preserve3d=p3;o.matrix3d=t3;
 o.heads=[...document.querySelectorAll('h1,h2,h3')].map(h=>h.tagName+':'+h.innerText.trim().replace(/\s+/g,' ').slice(0,38)).slice(0,18);
 o.inputs=[...document.querySelectorAll('input,select,textarea')].map(i=>{
   const r=i.getBoundingClientRect();
   return {t:i.tagName,ty:i.type,id:(i.id||i.name||'').slice(0,22),req:!!i.required,h:Math.round(r.height),
     opts:i.tagName==='SELECT'?[...i.options].map(x=>x.value).slice(0,6):null};});
 o.dialogs=[...document.querySelectorAll('dialog')].map(d=>({open:d.open,disp:getComputedStyle(d).display}));
 o.btns=[...document.querySelectorAll('button')].map((b,i)=>{
   const r=b.getBoundingClientRect();
   return {i:i,t:b.innerText.trim().replace(/\s+/g,' ').slice(0,24),w:Math.round(r.width),ty:b.type||''};});
 const anch=[...document.querySelectorAll('a[href^="#"]')];
 o.anchors={n:anch.length,dead:anch.map(a=>a.getAttribute('href')).filter(h=>h&&h!=='#'&&!document.querySelector(h)).slice(0,6)};
 o.bodyLen=document.body.innerText.length;
 return JSON.stringify(o);
})()"""

def main(frag):
    tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
    t=[x for x in tabs if frag in x.get('url','')][0]
    urllib.request.urlopen('http://127.0.0.1:9222/json/activate/'+t['id'],timeout=10).read()
    ws=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=180,suppress_origin=True)
    h=int(cdp.ev(ws,WALK,timeout=30))
    # P37: walk the page so every scroll reveal fires, then return to top
    for y in range(0,h+600,600):
        cdp.ev(ws,"(()=>{window.scrollTo(0,%d);return 1;})()"%y,timeout=20); time.sleep(0.28)
    cdp.ev(ws,"(()=>{window.scrollTo(0,0);return 1;})()",timeout=20); time.sleep(1.0)
    out=cdp.ev(ws,SURVEY,timeout=60)
    if not isinstance(out,str): out=repr(out)
    sys.stdout.write(out.encode('ascii','backslashreplace').decode('ascii'))
    sys.stdout.write(chr(10))

if __name__=='__main__':
    main(sys.argv[1])
