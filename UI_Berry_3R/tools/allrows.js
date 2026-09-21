(()=>{const rows=[];
document.querySelectorAll('tr').forEach(tr=>{const t=tr.innerText.split('\n').join(' | ').trim();
 if(t&&t.length>5) rows.push(t.slice(0,200));});
return JSON.stringify({n:rows.length,rows:rows.slice(0,15)});})()
