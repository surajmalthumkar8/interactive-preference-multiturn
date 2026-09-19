"""Read a task's server-side workflowStatus from a healthy Feather tab."""
import cdp, sys, json
uuid = sys.argv[1]
js = """(async()=>{
  const q={operationName:'T',variables:{},
    query:`query T { task(id:"%s") { id workflowStatus } }`};
  const r=await fetch('/api/graphql',{method:'POST',headers:{'content-type':'application/json'},
    credentials:'include',body:JSON.stringify([q])});
  return (await r.text()).slice(0,400);
})()""" % uuid
ws = cdp.conn('feather-prod.azure.com/?tab')
cdp.p(cdp.ev(ws, js, timeout=30))
