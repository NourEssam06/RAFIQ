(() => {
  const chapter=document.querySelector('.agent-story');
  const stage=chapter.querySelector('.agent-stage');
  const art=chapter.querySelector('.agent-art');
  const panels=[...chapter.querySelectorAll('.agent-panel')];
  const tabs=[...chapter.querySelectorAll('[data-chapter]')];
  const progressBar=chapter.querySelector('.agent-progress');
  const stacked=matchMedia('(prefers-reduced-motion:reduce)');
  const stops=[.17,.55,.92];
  let pose;
  try {pose=createAgentRobot(art)} catch {pose=createAgentTurntable(art)}
  let lastActive;
  const ease=t=>{const x=Math.max(0,Math.min(1,t));return x*x*(3-2*x)};
  function paint(progress,staticView) {
    const active=progress<.38?0:progress<.71?1:2;
    const angle=1.05*ease(progress/.22)+2.7*ease((progress-.25)/.30)+(2*Math.PI-3.75)*ease((progress-.58)/.32);
    pose(staticView?-.22:-angle);
    const visible=staticView?-1:active;
    if(visible!==lastActive){
      panels.forEach((panel,index)=>{panel.hidden=!staticView && index!==active});
      tabs.forEach((tab,index)=>{if(index===active)tab.setAttribute('aria-current','step');else tab.removeAttribute('aria-current')});
      lastActive=visible;
    }
    const distance=Math.min(Math.abs(progress-.38),Math.abs(progress-.71));
    const reveal=ease(Math.min(distance/.054,(progress+.018)/.085));
    panels[active].style.opacity=staticView?'':reveal;
    panels[active].style.transform=staticView?'':('translateY('+((1-reveal)*14)+'px)');
    if(staticView)panels.forEach(panel=>{panel.style.removeProperty('opacity');panel.style.removeProperty('transform')});
    progressBar.style.transform='scaleX('+progress+')';
  }
  gsap.registerPlugin(ScrollTrigger);
  const media=gsap.matchMedia();
  media.add('(prefers-reduced-motion: no-preference)',()=>{
    const playhead={progress:0};
    paint(0,false);
    gsap.to(playhead,{
      progress:1, ease:'none', onUpdate:()=>paint(playhead.progress,false),
      scrollTrigger:{trigger:chapter,start:'top top',end:'bottom bottom',scrub:.25,invalidateOnRefresh:true}
    });
  });
  media.add('(prefers-reduced-motion: reduce)',()=>{paint(0,true)});
  tabs.forEach((tab,index)=>tab.onclick=()=>window.scrollTo({top:scrollY+chapter.getBoundingClientRect().top+stops[index]*(chapter.offsetHeight-stage.offsetHeight),behavior:stacked.matches?'instant':'smooth'}));
  bindChoices('[data-session]',button=>{
    const descriptions=['Session 1 recorded no eye-closure warnings.','Session 2 recorded two eye-closure warnings.','This session recorded one eye-closure warning at 00:08.'];
    document.querySelector('#session-detail').textContent=descriptions[button.dataset.session];
  });
  const report=document.querySelector('.report');
  document.querySelector('#open-report').onclick=()=>{report.showModal();document.documentElement.style.overflow='hidden'};
  report.addEventListener('close',()=>{document.documentElement.style.overflow=''});

})();
