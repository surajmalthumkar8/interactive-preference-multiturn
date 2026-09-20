r"""Re-commit one reason textarea that failed to register in React state.

Section 21: Feather commits a reason on a REAL blur. fill3q.py blurs by clicking
(200,300), which is normally neutral, but if that point lands on something focusable
the blur does not commit and updateTaskStatus rejects with
'<field>_scoring_reason is a required property' inside an otherwise fine response.
This re-runs the chain for a single index and blurs onto the page heading instead,
checking the element under the blur point first.

Usage: python recommit.py <uuid> <textarea-index> <answers.json> <key>
"""
import sys, json, time
import cdp, mouse

uuid, idx, ansfile, key = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
txt = json.load(open(ansfile, encoding='utf-8'))[key]['reason']
ws = cdp.conn(uuid[:8])
raw = mouse.mkraw(ws)

cdp.ev(ws, "(()=>{document.querySelectorAll('textarea')[%d].scrollIntoView({block:'center'});return 1})()" % idx, timeout=25)
time.sleep(1.2)
pos = cdp.ev(ws, """(()=>{const t=document.querySelectorAll('textarea')[%d];
  const q=t.getBoundingClientRect();
  return JSON.stringify({x:Math.round(q.x+q.width/2),y:Math.round(q.y+q.height/2)});})()""" % idx, timeout=25)
p = json.loads(pos)
mouse.click_at(ws, p['x'], p['y'], settle=0.9)
for kk, code, vk, mod in [('a', 'KeyA', 65, 2), ('Delete', 'Delete', 46, 0)]:
    raw('Input.dispatchKeyEvent', {'type': 'keyDown', 'key': kk, 'code': code,
        'windowsVirtualKeyCode': vk, 'modifiers': mod})
    raw('Input.dispatchKeyEvent', {'type': 'keyUp', 'key': kk, 'code': code,
        'windowsVirtualKeyCode': vk, 'modifiers': mod})
    time.sleep(0.35)
raw('Input.insertText', {'text': txt})
time.sleep(1.0)

# pick a blur point that is provably inert
blur = cdp.ev(ws, """(()=>{
  for (const y of [120,150,90,60]) for (const x of [760,600,900]) {
    const e=document.elementFromPoint(x,y);
    if(!e) continue;
    if(e.closest('textarea,input,button,a,[role=button],[contenteditable]')) continue;
    return JSON.stringify({x,y,tag:e.tagName});
  }
  return JSON.stringify({x:200,y:300,tag:'FALLBACK'});})()""", timeout=25)
b = json.loads(blur)
cdp.p('blur on %s at %d,%d' % (b['tag'], b['x'], b['y']))
mouse.click_at(ws, b['x'], b['y'], settle=1.5)

got = cdp.ev(ws, "(()=>document.querySelectorAll('textarea')[%d].value.length)()" % idx, timeout=25)
cdp.p('%s idx %d want %d got %s' % (key, idx, len(txt), got))
