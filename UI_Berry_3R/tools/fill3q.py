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
        # Section 21. Feather commits a reason on a REAL blur, and a synthetic
        # .focus()/.blur() pair is not enough: the text sits in the DOM, the textarea
        # reads back the right length, and updateTaskStatus still rejects with
        # 'overall_scoring_reason is a required property' inside an HTTP 200.
        # What works: scroll it in, click it with the mouse, select-all + Delete by
        # keystroke, insertText, then click a neutral spot to blur it for real.
        cdp.ev(ws, """(()=>{const t=document.querySelectorAll('textarea')[%d];
          t.scrollIntoView({block:'center'}); return 1;})()""" % idx, timeout=25)
        time.sleep(1.2)
        pos = cdp.ev(ws, """(()=>{const t=document.querySelectorAll('textarea')[%d];
          const q=t.getBoundingClientRect();
          return JSON.stringify({x:Math.round(q.x+q.width/2),y:Math.round(q.y+q.height/2)});})()""" % idx, timeout=25)
        p = json.loads(pos)
        mouse.click_at(ws, p['x'], p['y'], settle=0.8)
        for kk, code, vk, mod in [('a','KeyA',65,2), ('Delete','Delete',46,0)]:
            raw('Input.dispatchKeyEvent', {'type':'keyDown','key':kk,'code':code,
                'windowsVirtualKeyCode':vk,'modifiers':mod})
            raw('Input.dispatchKeyEvent', {'type':'keyUp','key':kk,'code':code,
                'windowsVirtualKeyCode':vk,'modifiers':mod})
            time.sleep(0.3)
        raw('Input.insertText',{'text':txt})
        time.sleep(0.9)
        # Section 24 + P38. A fixed blur point is not always inert: on some layouts
        # (200,300) lands on a label that does nothing, the field never blurs, and
        # updateTaskStatus rejects with '<field>_scoring_reason is a required property'
        # inside an HTTP 200. Pick the blur target by hit test, just above the textarea.
        bt = cdp.ev(ws, """(()=>{const t=document.querySelectorAll('textarea')[%d];
          const q=t.getBoundingClientRect();
          for(let dy=-40;dy>-260;dy-=20){const y=Math.round(q.y+dy);if(y<60)break;
            const e=document.elementFromPoint(Math.round(q.x+q.width/2),y);
            if(e&&e.tagName!=='TEXTAREA'&&e.tagName!=='INPUT'&&e.tagName!=='BUTTON')
              return JSON.stringify({x:Math.round(q.x+q.width/2),y:y});}
          return JSON.stringify({x:200,y:300});})()""" % idx, timeout=25)
        bp = json.loads(bt)
        mouse.click_at(ws, bp['x'], bp['y'], settle=1.3)   # real blur, commits the field
        got=cdp.ev(ws,"(()=>document.querySelectorAll('textarea')[%d].value.length)()"%idx,timeout=25)
        # The DOM value can be right while React state is empty, which is exactly the
        # case Feather rejects. Check what React itself holds.
        rv=cdp.ev(ws,"""(()=>{const t=document.querySelectorAll('textarea')[%d];
          const k=Object.keys(t).find(x=>x.startsWith('__reactProps'));
          return k?String((t[k].value||'').length):'nokey';})()""" % idx, timeout=25)
        ok='OK' if (got==len(txt) and str(rv)==str(len(txt))) else 'MISMATCH'
        cdp.p('%-14s idx %d want %d dom %s react %s  %s' % (k, idx, len(txt), got, rv, ok))
        if ok!='OK': raise SystemExit('fill mismatch on '+k)

    # verify toggles stuck
    sel=cdp.ev(ws,"""(()=>{const g=[];document.querySelectorAll('.MuiToggleButtonGroup-root').forEach(x=>{
        g.push([...x.querySelectorAll('button')].filter(b=>b.className.indexOf('Mui-selected')>-1).map(b=>b.innerText.trim()));});
        return JSON.stringify(g);})()""",timeout=25)
    cdp.p('selected: '+str(sel))
    return ws

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2])
