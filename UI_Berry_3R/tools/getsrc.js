(async()=>{
 const f=[...document.querySelectorAll('iframe')].map(x=>x.src).filter(Boolean);
 const out=[];
 for(const u of f){
   try{
     const r=await fetch(u,{credentials:'include'});
     const t=await r.text();
     out.push({u:u, s:r.status, len:t.length});
   }catch(e){ out.push({u:u, err:String(e).slice(0,120)}); }
 }
 return JSON.stringify(out,null,1);
})()
