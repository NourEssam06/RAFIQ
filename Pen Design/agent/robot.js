/* Render the artist's local GLB with RAFIQ materials. */
function createAgentRobot(host) {
  THREE.ColorManagement.legacyMode = false;
  const scene = new THREE.Scene();
  const turntable = new THREE.Group();
  scene.add(turntable);
  const camera = new THREE.PerspectiveCamera(32, 1, .1, 30);
  const renderer = new THREE.WebGLRenderer({alpha:true, antialias:true,powerPreference:"high-performance"});
  renderer.outputEncoding = THREE.sRGBEncoding;
  renderer.setPixelRatio(1);
  renderer.setClearColor(0,0);
  host.append(renderer.domElement);
  const poster=new Image();
  poster.src='agent/robot-still.png';
  poster.alt='';
  poster.style.cssText='position:absolute;width:100%;height:100%;object-fit:contain';
  host.append(poster);
  const logoSvg="<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"472\" height=\"132\" viewBox=\"0 0 472 132\" role=\"img\" aria-label=\"RAFIQ\"><g transform=\"translate(399 66) scale(1 1)\"><circle r=\"42\" fill=\"none\" stroke=\"#FFFCE1\" stroke-width=\"8\"/><path fill=\"#FFFCE1\" d=\"M-39 -10 Q-24 -9 -11 -4 Q0 -10 11 -4 Q24 -9 39 -10 L40 -2 Q21 0 12 7 L7 17 L4 39 H-4 L-7 17 L-12 7 Q-21 0 -40 -2Z\"/></g><g fill=\"#FFFCE1\" fill-rule=\"evenodd\" transform=\"translate(24 40)\"><path d=\"M0 0H45Q64 0 64 17Q64 30 51 34L67 52H47L30 34H15V52H0ZM15 12V23H43Q49 23 49 17Q49 12 43 12Z\"/><path d=\"M69 52L94 0H115L141 52H124L119 41H91L86 52ZM97 29H114L105 10Z\"/><path d=\"M148 0H207V13H164V23H200V36H164V52H148Z\"/><path d=\"M216 0H232V52H216Z\"/><path d=\"M274 -1Q308 -1 308 26Q308 36 302 43L313 54H295L291 50Q284 53 274 53Q241 53 241 26Q241 -1 274 -1ZM274 12Q257 12 257 26Q257 40 274 40H280L270 30H288L291 33Q292 30 292 26Q292 12 274 12Z\"/></g></svg>";
  const logo=new THREE.TextureLoader().load('data:image/svg+xml;charset=utf-8,'+encodeURIComponent(logoSvg),render);
  scene.add(new THREE.HemisphereLight(0xf6f6eb,0x60737f,.95));
  function light(color,intensity,x,y,z) {
    const source=new THREE.DirectionalLight(color,intensity);
    source.position.set(x,y,z);
    scene.add(source);
  }
  light(0xfff2dc,1.7,-3,4,4);
  light(0xa6d9e5,1.1,4,1,2);
  light(0xd5ecff,2.2,2,4,-3);
  function render(){renderer.render(scene,camera)}
  function applyFinish(model){
    const material=model.getObjectByProperty('isMesh',true).material;
    material.metalness=.18;
    material.roughness=.62;
    material.onBeforeCompile=shader=>{
      shader.uniforms.rafiqMark={value:logo};
      shader.vertexShader='varying vec3 modelPoint;\n'+shader.vertexShader.replace('#include <begin_vertex>','#include <begin_vertex>\nmodelPoint=position;');
      shader.fragmentShader='uniform sampler2D rafiqMark; varying vec3 modelPoint;\n'+shader.fragmentShader.replace('#include <map_fragment>',`
        #include <map_fragment>
        vec3 atlas = diffuseColor.rgb;
        float luminance = dot(atlas, vec3(.2126,.7152,.0722));
        float faceLight = modelPoint.y < -.38 && modelPoint.z > .18 ? smoothstep(.08,.37,atlas.g-atlas.r) : 0.0;
        vec3 graphite = vec3(.022,.030,.033) + vec3(.065,.068,.07)*min(luminance,.5);
        if(modelPoint.y < -.30 && modelPoint.z < -.06 && modelPoint.z > -.38 && abs(modelPoint.x)<.28){
          graphite=vec3(.030,.038,.041);
          vec2 markUV=vec2(modelPoint.x/.49+.5,(modelPoint.z+.235)/.137+.5);
          if(all(greaterThanEqual(markUV,vec2(0.))) && all(lessThanEqual(markUV,vec2(1.)))){
            graphite=mix(graphite,vec3(.98,.955,.754),texture2D(rafiqMark,markUV).a);
          }
        }
        diffuseColor.rgb=mix(graphite,vec3(.0,.52,.76),faceLight);
      `);
    };
  }
  function attach(gltf){
    const model=gltf.scene;
    applyFinish(model);
    const box=new THREE.Box3().setFromObject(model);
    model.position.sub(box.getCenter(new THREE.Vector3()));
    turntable.add(model);
    host.dataset.model='miibot';
    poster.remove();
    render();
  }
  async function loadModel(){
    const loader=new THREE.GLTFLoader();
    // A compact derivative of the supplied GLB also loads directly from disk.
    await new Promise((resolve,reject)=>{
      const script=document.createElement('script');
      script.src='agent/miibot-preview.js';script.onload=resolve;script.onerror=reject;
      document.head.append(script);
    });
    const bytes=new Uint8Array(await (await fetch('data:application/octet-stream;base64,'+window.miibotGzip)).arrayBuffer());
    delete window.miibotGzip;
    const unpacked=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));
    attach(await loader.parseAsync(await new Response(unpacked).arrayBuffer(),''));
  }
  loadModel().catch(error=>{host.dataset.model='poster';console.warn('Miibot preview:',error)});
  new ResizeObserver(()=>{
    const {width,height}=host.getBoundingClientRect();
    if(!width || !height)return;
    camera.aspect=width/height;
    camera.position.set(0,.12,Math.max(4.15,3.45/camera.aspect));
    camera.lookAt(0,0,0);camera.updateProjectionMatrix();
    const scale=Math.min(1,420/width,490/height);
    renderer.setSize(Math.round(width*scale),Math.round(height*scale),false);render();
  }).observe(host);
  let lastAngle;
  return angle=>{
    if(lastAngle===angle)return;
    lastAngle=angle;turntable.rotation.y=angle;render();
  };
}
