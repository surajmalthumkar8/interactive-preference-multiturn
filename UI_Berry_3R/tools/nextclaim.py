"""Claim the next UI Berry task from the LinkedIn dispatcher, print WI + feather link."""
import sys, json, time
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import cdp
ws = cdp.conn('linkedin.com/ai-trainer')
cdp.ev(ws, "location.href='https://www.linkedin.com/ai-trainer/tasks?projectId=1253002&batchId=p-1868003'", awaitp=False)
time.sleep(13)
cdp.p(cdp.ev(ws, open('claim.js', encoding='utf-8').read(), timeout=30))
time.sleep(9)
cdp.p('fetch: '+str(cdp.ev(ws, "(()=>JSON.stringify(window.__fh||[]))()", timeout=25)))
