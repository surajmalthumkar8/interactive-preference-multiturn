(()=>{
  if(!window.__fh){ window.__fh=[]; const of=window.fetch;
    window.fetch=async function(...a){ const u=(typeof a[0]==='string'?a[0]:(a[0]&&a[0].url)||'');
      const m=(a[1]&&a[1].method)||'GET'; const r=await of.apply(this,a);
      if(u.includes('frontendAnnotationTaskResults')) window.__fh.push({u:u.slice(0,120),m,s:r.status});
      return r; }; }
  const b=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Submit');
  if(!b) return 'NO SUBMIT';
  const f=b.closest('form');
  if(!f) return 'NO FORM';
  f.requestSubmit(b);
  return 'requestSubmit fired';
})()
