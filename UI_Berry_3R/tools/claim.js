(()=>{
  const b = document.querySelector('button.ant-dropdown-trigger');
  if(!b) return 'NO TRIGGER BUTTON';
  const key = Object.keys(b).find(k => k.startsWith('__reactFiber$'));
  if(!key) return 'NO FIBER KEY';
  let f = b[key], menu = null, hops = 0;
  while (f && hops < 25) {
    const p = f.memoizedProps;
    if (p && p.menu && Array.isArray(p.menu.items)) { menu = p.menu; break; }
    f = f.return; hops++;
  }
  if(!menu) return 'NO MENU FOUND';
  const item = menu.items.find(i => i.key === 'ANNOTATION');
  if(!item) return 'NO ANNOTATION ITEM; keys=' + menu.items.map(i=>i.key).join(',');
  item.onClick({ key:'ANNOTATION', domEvent:{ stopPropagation(){}, preventDefault(){} } });
  return 'ANNOTATION onClick invoked';
})()
