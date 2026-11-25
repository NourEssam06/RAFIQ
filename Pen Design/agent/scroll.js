/* Follow native scrolling with a short time-based settle, independently of refresh rate. */
function trackScroll(section, stage, staticMode, paint) {
  let top, travel, shown, previousTime, frame=0;
  function target(){return Math.max(0,Math.min(1,(scrollY-top)/travel))}
  function measure(){
    top=section.getBoundingClientRect().top+scrollY;
    travel=Math.max(1,section.offsetHeight-stage.offsetHeight);
    shown=target();
    paint(shown,staticMode.matches);
  }
  function tick(time){
    frame=0;
    const goal=target();
    const elapsed=Math.min(64,time-previousTime);
    previousTime=time;
    shown+=(goal-shown)*(1-Math.exp(-elapsed/78));
    if(Math.abs(goal-shown)<.00015)shown=goal;
    paint(shown,false);
    if(shown!==goal) frame=requestAnimationFrame(tick);
  }
  function schedule(){
    if(frame || staticMode.matches || shown===target()) return;
    previousTime=performance.now();
    frame=requestAnimationFrame(tick);
  }
  function reset(){
    cancelAnimationFrame(frame);frame=0;measure();
  }
  addEventListener('scroll',schedule,{passive:true});
  addEventListener('resize',reset);
  staticMode.addEventListener('change',reset);
  new ResizeObserver(reset).observe(section);
  measure();
}
