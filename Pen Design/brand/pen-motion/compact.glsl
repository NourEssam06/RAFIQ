precision mediump float;
/** @resolution */
uniform vec2 resolution;
/** @time */
uniform float seconds;
void main() {
    vec2 p = (gl_FragCoord.xy / resolution - 0.5) * 24.0;
    float angle = mod(atan(-p.y, p.x) - seconds * 6.283185 + 12.56637, 6.283185);
    float end = 31.0 / 8.0;
    float d = abs(length(p) - 8.0);
    if (angle > end) d = min(length(p) + 8.0, sqrt(max(0.0, dot(p,p) + 64.0 - 16.0*length(p)*max(cos(angle),cos(angle-end)))));
    float alpha = 1.0 - smoothstep(0.75,1.75,d);
    gl_FragColor = vec4(vec3(0.0,0.7294,0.8863)*alpha,alpha);
}
