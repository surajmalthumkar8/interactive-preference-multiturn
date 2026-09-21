(()=>{
 const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Submit');
 if(!b) return 'no submit';
 const q=b.getBoundingClientRect();
 const cx=q.x+q.width/2, cy=q.y+q.height/2;
 const mk=(t,ctor)=>new ctor(t,{bubbles:true,cancelable:true,composed:true,
   clientX:cx,clientY:cy,button:0,buttons:1,pointerId:1,pointerType:'mouse',isPrimary:true});
 b.scrollIntoView({block:'center'});
 ['pointerover','pointerenter','pointerdown'].forEach(t=>b.dispatchEvent(mk(t,PointerEvent)));
 b.dispatchEvent(mk('mousedown',MouseEvent));
 b.focus();
 b.dispatchEvent(mk('pointerup',PointerEvent));
 b.dispatchEvent(mk('mouseup',MouseEvent));
 b.dispatchEvent(mk('click',MouseEvent));
 return 'dispatched at '+Math.round(cx)+','+Math.round(cy);
})()
