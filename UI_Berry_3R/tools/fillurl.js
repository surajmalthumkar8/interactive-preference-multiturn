// Fill LinkedIn's Attempt URL input with the CLAIMED Feather task uuid.
// Replace __UUID__ before evaluating, or use the python wrapper.
// The native value setter is required: a plain assignment leaves React's
// state unchanged and the field submits empty (LINKEDIN_PLATFORM.md section 15).
(()=>{
  const i=document.getElementById('ATTEMPT_URL-link-single');
  if(!i) return 'NO INPUT';
  const url='https://msft.feather-prod.azure.com/tasks/__UUID__';
  const setter=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;
  i.focus();
  setter.call(i,url);
  i.dispatchEvent(new Event('input',{bubbles:true}));
  i.dispatchEvent(new Event('change',{bubbles:true}));
  return 'set -> '+i.value;
})()
