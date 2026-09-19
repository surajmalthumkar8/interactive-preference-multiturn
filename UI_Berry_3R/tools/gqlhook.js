(()=>{
  if(window.__gql) return 'already';
  window.__gql=[];
  const of=window.fetch;
  window.fetch=async function(...a){
    const url=(typeof a[0]==='string'?a[0]:(a[0]&&a[0].url)||'');
    let body=null;
    try{ body=(a[1]&&a[1].body)?String(a[1].body):null; }catch(e){}
    const res=await of.apply(this,a);
    if(url.includes('graphql')||url.includes('/api/')){
      let out='';
      try{ out=await res.clone().text(); }catch(e){ out='<unreadable>'; }
      window.__gql.push({u:url.slice(0,120), req:(body||'').slice(0,900), s:res.status, res:out.slice(0,400)});
    }
    return res;
  };
  return 'gql hook installed';
})()
