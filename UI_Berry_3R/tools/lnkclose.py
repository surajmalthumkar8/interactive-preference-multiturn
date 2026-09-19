"""Close a UI Berry task on LinkedIn: fill the Attempt URL with the REAL uuid, submit.
Usage: python lnkclose.py <workitem-id> <real-feather-uuid>"""
import sys, json, time
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp
wi, uuid = sys.argv[1], sys.argv[2]
ws = cdp.conn('linkedin.com/ai-trainer')
cdp.ev(ws, "location.href='https://www.linkedin.com/ai-trainer/tasks/%s'" % wi, awaitp=False)
time.sleep(11)
src = open('fillurl.js', encoding='utf-8').read().replace('__UUID__', uuid)
cdp.p(cdp.ev(ws, src, timeout=25))
time.sleep(1.5)
cdp.p(cdp.ev(ws, open('lnksubmit.js', encoding='utf-8').read(), timeout=25))
time.sleep(9)
cdp.p('fetch: '+str(cdp.ev(ws, "(()=>JSON.stringify(window.__fh||[]))()", timeout=25)))
