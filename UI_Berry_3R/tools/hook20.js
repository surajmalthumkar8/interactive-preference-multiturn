(()=>{
  if(window.__fh2) return 'already hooked';
  window.__fh2=[];
  const of=window.fetch;
  window.fetch=async function(...a){
    const u=(typeof a[0]==='string'?a[0]:(a[0]&&a[0].url)||'');
    const m=(a[1]&&a[1].method)||'GET';
    const r=await of.apply(this,a);
    if(u.indexOf('frontendAnnotationTaskResults')>-1){
      let body='';
      try{ body=await r.clone().text(); }catch(e){ body='<unreadable>'; }
      window.__fh2.push({u:u.slice(0,140),m:m,s:r.status,b:body.slice(0,300)});
    }
    return r;
  };
  return 'hooked';
})()
