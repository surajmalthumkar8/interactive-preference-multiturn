import sys,json,base64,urllib.request,websocket,time
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import mouse
frag=sys.argv[1]; name=sys.argv[2]; frac=float(sys.argv[3])
tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
t=[x for x in tabs if frag in x.get('url','')][0]
urllib.request.urlopen('http://127.0.0.1:9222/json/activate/'+t['id'],timeout=10).read()
ws=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=120,suppress_origin=True)
raw=mouse.mkraw(ws); raw('Page.enable',{}); raw('Page.bringToFront',{}); time.sleep(0.8)
m=raw('Runtime.evaluate',{'expression':"(()=>{const m=window.visualViewport;return JSON.stringify({w:innerWidth,h:innerHeight});})()",'returnByValue':True})
vp=json.loads(m['result']['result']['value']); H=vp['h']
SB_X=1495
TOP=136; BOT=H-16
y=TOP+(BOT-TOP)*frac
raw('Input.dispatchMouseEvent',{'type':'mousePressed','x':SB_X,'y':int(TOP+6),'button':'left','clickCount':1})
time.sleep(0.2)
raw('Input.dispatchMouseEvent',{'type':'mouseMoved','x':SB_X,'y':int(y),'button':'left'})
time.sleep(0.5)
raw('Input.dispatchMouseEvent',{'type':'mouseReleased','x':SB_X,'y':int(y),'button':'left','clickCount':1})
time.sleep(2.4)
s=raw('Page.captureScreenshot',{'format':'png'})
open(r'C:\Users\Suraj\.claude\playwright-output\%s.png'%name,'wb').write(base64.b64decode(s['result']['data']))
print('saved',name,'vp',vp)
