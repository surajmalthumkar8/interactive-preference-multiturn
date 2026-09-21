import json,urllib.request
tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
pages=[t for t in tabs if t.get('type')=='page']
closed=0; kept_board=False; kept_camp=False
for t in pages:
    u=t.get('url','')
    if 'ai-trainer/tasks?projectId' in u and not kept_board:
        kept_board=True; continue
    if 'feather-prod.azure.com/campaigns/' in u and not kept_camp:
        kept_camp=True; continue
    if ('ai-trainer/tasks/' in u) or ('feather-prod.azure.com/tasks/' in u) \
       or ('.c.msft.feather-prod' in u) or ('feather-prod.azure.com/campaigns/' in u):
        try:
            urllib.request.urlopen('http://127.0.0.1:9222/json/close/'+t['id'],timeout=8).read(); closed+=1
        except Exception: pass
print('closed',closed)
tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
print('pages now:',len([t for t in tabs if t.get('type')=='page']))
