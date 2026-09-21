(()=>{
 const want="Website A";
 const tabs=[...document.querySelectorAll('[role=tab]')];
 const b=tabs.find(x=>x.innerText.trim()===want);
 if(!b) return 'NOT FOUND: '+JSON.stringify(tabs.map(x=>x.innerText.trim()));
 b.scrollIntoView({block:'center'});
 const q=b.getBoundingClientRect();
 return JSON.stringify({x:Math.round(q.x+q.width/2),y:Math.round(q.y+q.height/2),sel:b.getAttribute('aria-selected')});
})()
