(async()=>{
 const u=URLHERE;
 const r=await fetch(u,{credentials:'include'});
 const t=await r.text();
 const d=new DOMParser().parseFromString(t,'text/html');
 const q=s=>d.querySelectorAll(s).length;
 return JSON.stringify({
   cards:q('.property-card, .listing-card, [class*=card]'),
   navlinks:q('nav a'),
   selects:q('select'),
   selOpts:[...d.querySelectorAll('select')].map(s=>s.id+':'+s.options.length),
   forms:[...d.querySelectorAll('form')].map(f=>f.id||f.className||'form'),
   reqFields:q('[required]'),
   waLinks:[...d.querySelectorAll('a[href*="wa.me"],a[href*="whatsapp"]')].map(a=>a.getAttribute('href').slice(0,60)),
   telLinks:[...d.querySelectorAll('a[href^="tel:"]')].map(a=>a.getAttribute('href')),
   sections:[...d.querySelectorAll('section')].map(s=>s.id||s.className.split(' ')[0]).slice(0,20)
 },null,1);
})()
