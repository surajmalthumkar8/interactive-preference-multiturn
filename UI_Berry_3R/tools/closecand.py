r"""Close stale candidate tabs (the *.c.msft.feather-prod origins).

Candidate tabs have to be opened outside the nogl hook so their canvases are
real, which means they accumulate fast. Left alone they bury the task tab, and
fill3q.py finds that tab by uuid[:8], so a stale tab set makes it fail with a
bare IndexError. Run this after every evaluation.

Keeps: the task page, the campaign/todo pages, LinkedIn, anything non-Feather.
"""
import json, re, urllib.request

CAND = re.compile(r'https://[a-z0-9]{12,}\.c\.msft\.feather-prod\.azure\.com')
tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list', timeout=8).read().decode())
n = 0
for t in tabs:
    if t.get('type') != 'page':
        continue
    if CAND.match(t.get('url', '')):
        try:
            urllib.request.urlopen('http://127.0.0.1:9222/json/close/' + t['id'], timeout=8).read()
            n += 1
        except Exception as e:
            print('skip %s: %s' % (t['id'][:8], e))
print('closed %d candidate tab(s)' % n)
