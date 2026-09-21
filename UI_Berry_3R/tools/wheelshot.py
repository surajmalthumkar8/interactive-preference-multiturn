import sys,json,base64,urllib.request,websocket,time
sys.path.insert(0, r'C:\Users\Suraj\Downloads\project_interactive_linkedin\UI_Berry_3R\tools')
import mouse
frag=sys.argv[1]; name=sys.argv[2]; ticks=int(sys.argv[3])
X=int(sys.argv[4]) if len(sys.argv)>4 else 950
tabs=json.loads(urllib.request.urlopen('http://127.0.0.1:9222/json/list',timeout=8).read().decode())
t=[x for x in tabs if frag in x.get('url','')][0]
urllib.request.urlopen('http://127.0.0.1:9222/json/activate/'+t['id'],timeout=10).read()
ws=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=120,suppress_origin=True)
raw=mouse.mkraw(ws); raw('Page.enable',{}); raw('Page.bringToFront',{}); time.sleep(0.8)
Y=600
raw('Input.dispatchMouseEvent',{'type':'mouseMoved','x':X,'y':Y})
time.sleep(0.3)
mid=[1000]
def fire(p):
    mid[0]+=1
    ws.send(json.dumps({'id':mid[0],'method':'Input.dispatchMouseEvent','params':p}))
for i in range(abs(ticks)):
    fire({'type':'mouseWheel','x':X,'y':Y,'deltaX':0,
          'deltaY':(400 if ticks>0 else -400),'pointerType':'mouse'})
    time.sleep(0.30)
time.sleep(2.2)
# drain socket, then screenshot on a fresh connection
ws.close()
ws2=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=120,suppress_origin=True)
raw2=mouse.mkraw(ws2); raw2('Page.enable',{}); time.sleep(0.4)
s=raw2('Page.captureScreenshot',{'format':'png'})
open(r'C:\Users\Suraj\.claude\playwright-output\%s.png'%name,'wb').write(base64.b64decode(s['result']['data']))
print('saved',name)
