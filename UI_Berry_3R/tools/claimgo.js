(async()=>{
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const open=()=>{const b=[...document.querySelectorAll('button')].find(x=>/Unclaimed/i.test(x.innerText.trim()));
    if(!b)return false;
    ['pointerdown','mousedown','pointerup','mouseup','click'].forEach(t=>
      b.dispatchEvent(new (t.startsWith('pointer')?PointerEvent:MouseEvent)(t,{bubbles:true,cancelable:true,composed:true,button:0})));
    return true;};
  if(!open()) return 'already claimed or no btn';
  await sleep(2500);
  const it=[...document.querySelectorAll('[role="menuitem"]')].find(e=>e.innerText.trim()==='Claim task');
  if(!it) return 'no claim item';
  ['pointerdown','mousedown','pointerup','mouseup','click'].forEach(t=>
    it.dispatchEvent(new (t.startsWith('pointer')?PointerEvent:MouseEvent)(t,{bubbles:true,cancelable:true,composed:true,button:0})));
  await sleep(9000);
  const p=document.getElementById('radix-:rf:-content-layout_node_4');
  const re=new RegExp('https?://[a-z0-9]+[.]c[.]msft[.]feather-prod[.]azure[.]com','g');
  return JSON.stringify({status:(document.querySelector('button.hdk-inline-flex')||{}).innerText||'',
    chip:[...document.querySelectorAll('button')].map(x=>x.innerText.trim()).filter(t=>/Unclaimed|In progress|Claimed/i.test(t)),
    panel:p?p.innerText.slice(0,90):'none',
    iframes:[...document.querySelectorAll('iframe')].map(f=>f.src),
    hosts:[...new Set(document.documentElement.outerHTML.match(re)||[])]});
})()
