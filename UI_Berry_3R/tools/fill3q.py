"""Fill + submit a DA0518 3-question Feather task. Applies LINKEDIN_PLATFORM.md 19c/19d.
Usage: python fill3q.py <task-uuid> <answers.json>
answers.json: {"aesthetics":{"option":"A","reason":"..."}, "functionality":{...}, "overall":{...}}
Options map: A -> "A is better", B -> "B is better", BOTH_GOOD, BOTH_BAD.
"""
import sys, json, time, urllib.request, websocket
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp, mouse

LABEL = {"A":"A is better","B":"B is better","BOTH_GOOD":"Both are good","BOTH_BAD":"Both are bad"}
ORDER = ["aesthetics","functionality","overall"]

def connect(frag):
    tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
    t=[x for x in tabs if frag in x.get('url','')][0]
    urllib.request.urlopen('http://127.0.0.1:9222/json/activate/'+t['id'],timeout=10).read()
    ws=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=120,suppress_origin=True)
    raw=mouse.mkraw(ws); raw('Page.enable',{}); raw('Page.bringToFront',{}); time.sleep(1)
    return ws, raw

def main(uuid, ansfile):
    d=json.load(open(ansfile,encoding='utf-8'))
    ws,raw=connect(uuid[:8])

    # 19c: only visible textareas are real; odd indices are sizing mirrors
    idxs=json.loads(cdp.ev(ws,"""(()=>JSON.stringify([...document.querySelectorAll('textarea')]
        .map((t,i)=>({i:i,h:t.getBoundingClientRect().height}))
        .filter(o=>o.h>0).map(o=>o.i)))()""",timeout=30))
    cdp.p('real textareas: '+str(idxs))
    assert len(idxs)==3, 'expected 3 visible textareas, got %r' % (idxs,)

    # 19d: set each toggle group separately via React onClick
    for gi,k in enumerate(ORDER):
        want=LABEL[d[k]["option"]]
        r=cdp.ev(ws,"""(()=>{
          const g=document.querySelectorAll('.MuiToggleButtonGroup-root')[%d];
          if(!g) return 'no group';
          const b=[...g.querySelectorAll('button')].find(x=>x.innerText.trim()===%s);
          if(!b) return 'no option';
          if(b.className.indexOf('Mui-selected')>-1) return 'already';
          b.scrollIntoView({block:'center'});
          const pk=Object.keys(b).find(x=>x.startsWith('__reactProps'));
          if(pk&&b[pk].onClick){b[pk].onClick({preventDefault(){},stopPropagation(){},currentTarget:b,target:b,type:'click'});return 'react';}
          b.click(); return 'dom';
        })()""" % (gi, json.dumps(want)), timeout=25)
        cdp.p('%-14s %-14s -> %s' % (k, want, r))
        time.sleep(1.4)

    # fill reasons
    for k,idx in zip(ORDER, idxs):
        txt=d[k]["reason"]
        # section 21: clear via the native setter, type, then fire change + blur.
        # Feather commits a reason field on blur; without it the text stays in the DOM
        # only and updateTaskStatus rejects with 'is a required property' inside a 200.
        cdp.ev(ws,"""(()=>{const t=document.querySelectorAll('textarea')[%d];
          t.scrollIntoView({block:'center'});
          const s=Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype,'value').set;
          s.call(t,''); t.dispatchEvent(new Event('input',{bubbles:true}));
          t.focus(); return 1;})()""" % idx, timeout=25)
        time.sleep(0.6)
        raw('Input.insertText',{'text':txt})
        time.sleep(0.8)
        cdp.ev(ws,"""(()=>{const t=document.querySelectorAll('textarea')[%d];
          t.dispatchEvent(new Event('change',{bubbles:true})); t.blur(); return 1;})()""" % idx, timeout=25)
        time.sleep(1.0)
        got=cdp.ev(ws,"(()=>document.querySelectorAll('textarea')[%d].value.length)()"%idx,timeout=25)
        ok='OK' if got==len(txt) else 'MISMATCH'
        cdp.p('%-14s idx %d want %d got %s  %s' % (k, idx, len(txt), got, ok))
        if got!=len(txt): raise SystemExit('fill mismatch on '+k)

    # verify toggles stuck
    sel=cdp.ev(ws,"""(()=>{const g=[];document.querySelectorAll('.MuiToggleButtonGroup-root').forEach(x=>{
        g.push([...x.querySelectorAll('button')].filter(b=>b.className.indexOf('Mui-selected')>-1).map(b=>b.innerText.trim()));});
        return JSON.stringify(g);})()""",timeout=25)
    cdp.p('selected: '+str(sel))
    return ws

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2])
