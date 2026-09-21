(()=>{ if(window.__wi) return 'already';
 window.__wi=[];
 const of=window.fetch;
 window.fetch=async function(...a){
   const u=(typeof a[0]==='string')?a[0]:(a[0]&&a[0].url)||'';
   const r=await of.apply(this,a);
   if(/frontendAnnotationTaskResults|updateTask|submit/i.test(u)){
     try{ const c=r.clone(); const b=await c.text();
       window.__wi.push({u:u.slice(0,140), s:r.status, b:b.slice(0,400)}); }catch(e){}
   }
   return r;
 };
 return 'hooked';
})()
