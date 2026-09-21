(async()=>{
 const u=URLHERE;
 // load into a hidden same-origin-ish probe frame is not possible cross-origin;
 // instead re-fetch and execute nothing - report render fn + data counts statically
 const r=await fetch(u,{credentials:'include'}); const t=await r.text();
 const m=t.match(/const\s+(properties|listings|PROPERTIES)\s*=\s*\[/);
 let n=0;
 if(m){ const i=t.indexOf(m[0]); let depth=0,j=i+m[0].length-1;
   for(;j<t.length;j++){const c=t[j]; if(c==='[')depth++; else if(c===']'){depth--; if(!depth)break;}}
   const blob=t.slice(i,j+1); n=(blob.match(/\{\s*(id|name|title)\s*:/g)||[]).length;
 }
 return JSON.stringify({dataVar:m?m[1]:null, records:n,
   renderFns:(t.match(/function\s+render\w*/g)||[]),
   innerHTMLwrites:(t.match(/innerHTML\s*=/g)||[]).length,
   domContentLoaded:(t.match(/DOMContentLoaded/g)||[]).length});
})()
