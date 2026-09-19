(()=>{
  // Neuter WebGL so Three.js cannot spin up a render loop
  try{
    const bad=function(){ return null; };
    HTMLCanvasElement.prototype.getContext = bad;
  }catch(e){}
  // Stop animation loops cold
  try{ window.requestAnimationFrame=function(){ return 0; }; }catch(e){}
  window.__noglInstalled=true;
})()
