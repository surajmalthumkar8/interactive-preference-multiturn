"""Run the Feather submit chain on an already-open, rendered task tab.
Usage: python submitchain.py <feather-task-uuid>"""
import cdp, mouse, json, time, sys

uuid = sys.argv[1]

def click_text(ws, text, settle=2.5, scope='button'):
    js = ("(()=>{const e=[...document.querySelectorAll('%s,[role=menuitem],li,[role=option]')]"
          ".find(x=>x.innerText.trim()===%s);if(!e)return 'null';"
          "e.scrollIntoView({block:'center'});const r=e.getBoundingClientRect();"
          "return JSON.stringify({x:Math.round(r.left+r.width/2),y:Math.round(r.top+r.height/2)});})()"
          ) % (scope, json.dumps(text))
    c = cdp.ev(ws, js, timeout=25)
    if not c or c == 'null':
        return False
    c = json.loads(c)
    mouse.click_at(ws, c['x'], c['y'], settle=settle)
    return True

ws = cdp.conn('tasks/' + uuid[:8])
cdp.p('pre-submit check: ' + str(cdp.ev(ws, open('verify.js').read(), timeout=25)))
assert click_text(ws, 'In progress'), 'no status pill'
assert click_text(ws, 'Mark as complete', settle=3.0), 'no Mark as complete'
time.sleep(1.5)
assert click_text(ws, 'Submit Task', settle=4.0), 'no Submit Task'
time.sleep(5)
cdp.p('clicked Submit Task; verify server-side next')
