/* These views were rendered from the RAFIQ-styled Miibot GLB, 3 degrees apart. */
function createAgentTurntable(host) {
  const width=384, height=448, frames=120, perSheet=12;
  const canvas=document.createElement('canvas');
  canvas.width=width;canvas.height=height;
  canvas.style.cssText='width:100%;height:100%;object-fit:contain';
  const context=canvas.getContext('2d');
  const poster=new Image();
  poster.src='agent/robot-still.png';poster.alt='';
  host.replaceChildren(poster);
  if(!context)return ()=>{};
  const sheets=[];
  let desired=0, last=-1;
  function drawCell(index,alpha){
    const sheet=sheets[Math.floor(index/perSheet)];
    if(!sheet?.ready)return false;
    const cell=index%perSheet;
    context.globalAlpha=alpha;
    context.drawImage(sheet.image,(cell%4)*width,Math.floor(cell/4)*height,width,height,0,0,width,height);
    return true;
  }
  function display(){
    if(last===desired)return;
    const first=Math.floor(desired), next=(first+1)%frames;
    if(!sheets[Math.floor(first/perSheet)]?.ready || !sheets[Math.floor(next/perSheet)]?.ready)return;
    if(!canvas.isConnected){host.replaceChildren(canvas);host.dataset.model='miibot'}
    context.clearRect(0,0,width,height);
    drawCell(first,1);
    const fraction=desired-first;
    if(fraction>.02)drawCell(next,fraction);
    last=desired;
  }
  async function load(i){
    if(sheets[i])return;
    const image=new Image();
    sheets[i]={image,ready:false};
    image.src='agent/turntable/pose-'+i+'.webp';
    try {await image.decode();sheets[i].ready=true;display()} catch { /* Keep the last available pose. */ }
  }
  const observer=new IntersectionObserver(async entries=>{
    if(!entries.some(entry=>entry.isIntersecting))return;
    observer.disconnect();
    for(let i=0;i<frames/perSheet;i++)await load(i);
  },{rootMargin:'150% 0px'});
  observer.observe(host);
  return angle=>{
    desired=(((-angle/(2*Math.PI)*frames)%frames)+frames)%frames;
    display();
  };
}
