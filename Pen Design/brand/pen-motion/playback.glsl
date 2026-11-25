precision highp float;
/** @resolution */
uniform vec2 resolution;
/** @time */
uniform float seconds;
uniform sampler2D frames;
uniform vec2 grid;
uniform float framesPerSecond;
uniform float introFrames;
uniform float loopFrames;
void main() {
    float tick = floor(seconds * framesPerSecond);
    float frame = tick < introFrames ? tick : introFrames + mod(tick - introFrames, loopFrames);
    // The canvas thumbnail is rendered at time zero. Show the complete lockup there.
    if (seconds == 0.0 && introFrames > 0.0) frame = introFrames;
    vec2 cell = vec2(mod(frame, grid.x), grid.y - 1.0 - floor(frame / grid.x));
    vec2 pixel = 0.5 / (vec2(textureSize(frames, 0)) / grid);
    vec2 uv = clamp(gl_FragCoord.xy / resolution, pixel, 1.0 - pixel);
    gl_FragColor = texture2D(frames, (cell + uv) / grid);
}
