(()=>{
  const tas=[...document.querySelectorAll('textarea')].map((t,i)=>({i,len:(t.value||'').length}));
  const opts=[...document.querySelectorAll('button')]
    .filter(b=>/^(A is better|B is better|Both are good|Both are bad)$/.test(b.innerText.trim()));
  const picked=[];
  for(let q=0;q<opts.length;q+=4){
    const g=opts.slice(q,q+4).find(b=>b.getAttribute('aria-pressed')==='true');
    picked.push(g?g.innerText.trim():'NONE');
  }
  return JSON.stringify({textareas:tas,verdicts:picked},null,1);
})()
