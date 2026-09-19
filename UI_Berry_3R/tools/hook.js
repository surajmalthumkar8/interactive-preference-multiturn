(()=>{
  if(window.__claimLog) return 'already';
  window.__claimLog=[];
  const of=window.fetch;
  window.fetch=async function(...a){
    const url=(typeof a[0]==='string'?a[0]:(a[0]&&a[0].url)||'');
    const res=await of.apply(this,a);
    if(url.toLowerCase().includes('claim')){
      let body='';
      try{ body=await res.clone().text(); }catch(e){ body='<unreadable>'; }
      window.__claimLog.push({u:url.slice(0,150),s:res.status,b:body.slice(0,400)});
    }
    return res;
  };
  return 'hook installed';
})()
