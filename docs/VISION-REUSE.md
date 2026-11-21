# Reusing a driver-monitoring model in RAFIQ

**Selected for v1, pending qualification.** Adapt Driver Monitor's browser worker and face and hand cue extraction. Use the pretrained MediaPipe Face and Hand Landmarker models and OpenCV Zoo NanoDet as one pipeline in M02. NanoDet is the sole object detector. RAFIQ applies its own temporal behavior rules using the combined cues. [M02 architecture](ARCHITECTURE.md#module-m02--on-device-monitoring) · [TRD vision contract](TRD.md#21-pretrained-browser-vision)

RAFIQ requires local CPU inference in Chrome on Windows 11, offline operation after setup, and separate, potentially overlapping observations for drowsiness, distraction, active phone use, eating, and drinking. The reference camera sees the driver's face and upper body. [PRD §8](PRD.md#8-planning-decisions-and-release-gates) · [On-device monitoring architecture](ARCHITECTURE.md#module-m02--on-device-monitoring)

## Selected components

| Component | Reuse in RAFIQ | Provenance and terms |
| --- | --- | --- |
| Driver Monitor browser code | Adapt worker scheduling, face cue extraction, and hand-landmark processing for M02. | Pin a reviewed commit and retain its MIT notice. [Project](https://github.com/iice257/driver-monitor) · [MIT license](https://github.com/iice257/driver-monitor/blob/main/LICENSE) |
| Google MediaPipe | Run `face_landmarker.task` and `hand_landmarker.task` using Tasks Vision on CPU. Extract eye closure, gaze and head pose cues, plus hand position and movement. | Verify provenance and redistribution terms for each exact task bundle separately from the adapted source and runtime licenses. [Face Landmarker](https://developers.google.com/edge/mediapipe/solutions/vision/face_landmarker) · [Hand Landmarker](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker) |
| OpenCV Zoo NanoDet | Run `object_detection_nanodet_2022nov.onnx` in ONNX Runtime Web with WebAssembly. Detect phones, cups, bottles, utensils and supported food categories. Adapt preprocessing and box decoding from the reference. | The upstream directory applies Apache-2.0 to its files, including the model. Pin the source revision and verify the actual model bytes from Git LFS before packaging. [Model and license](https://github.com/opencv/opencv_zoo/tree/main/models/object_detection_nanodet) · [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/) |

## Other models reviewed

| Candidate | Evidence and adoption decision |
| --- | --- |
| **AlbatrossC Driver Monitoring System** | Closest match by label. The YOLO11n ONNX model includes all five baseline labels and runs in an ONNX Runtime Web demo for uploaded images. The drinking label can include a nearby beverage. The repository and available weights have no verified reuse license, so it serves as a reference for the capabilities. [Project and labels](https://github.com/AlbatrossC/Driver-Monitoring-System) · [ONNX files](https://github.com/AlbatrossC/Driver-Monitoring-System/tree/main/public/static/models) |
| **Inferensys Bulwark E1** | Video model with an ONNX CPU research preview. The published weights are restricted to non-commercial research and explicitly exclude product demos. Upstream reports weak eye-closure and held-out camera results for E1 v0. [Bulwark licenses and evaluation](https://github.com/Inferensys/bulwark#licences) |
| **Intel Open Model Zoo driver action recognition** | The encoder and decoder manifests identify Apache-2.0 weights. They ship as OpenVINO IR. The driver labels include texting and calling, combine eating with drinking, and lack drowsiness. This is a possible native benchmark. [Encoder manifest](https://github.com/openvinotoolkit/open_model_zoo/blob/master/models/intel/driver-action-recognition-adas-0002/driver-action-recognition-adas-0002-encoder/model.yml) · [Decoder manifest](https://github.com/openvinotoolkit/open_model_zoo/blob/master/models/intel/driver-action-recognition-adas-0002/driver-action-recognition-adas-0002-decoder/model.yml) · [Driver action labels](https://github.com/openvinotoolkit/open_model_zoo/blob/master/demos/action_recognition_demo/python/driver_actions.txt) |

## RAFIQ adjustments

1. Replace the upstream sample's phone-only detection path with NanoDet. Calibrate the frame cadence and the cue freshness window on the reference device. Emit timestamped cues and per-class availability to RAFIQ's evaluator. Evaluate distraction independently when phone use also qualifies. [Upstream frame scheduling](https://github.com/iice257/driver-monitor/blob/main/web/app.js) · [RAFIQ pipeline](TRD.md#21-pretrained-browser-vision)
2. Require active interaction for phone use. Use hand-to-mouth motion and the associated object class to evaluate eating and drinking separately. Include an unused phone, an empty hand near the ear, holding a cup, talking, and occluded cues in the controlled fixtures. A class with missing evidence is unavailable during that interval. [Benchmark and behavior policy](PRD.md#83-benchmark-and-behavior-policy)
3. Record the exact upstream revisions, runtime versions, artifact sources, licenses, notices, and SHA-256 hashes in the bundle manifest. Verify setup and run the 30-minute offline CPU test with the same bundle used for 10 Hz held-out scoring. Gate any behavior that misses its targets. Training or fine-tuning requires a separate decision. [Asset packaging](DOCKER.md#pretrained-vision-assets) · [Acceptance gates](TRD.md#8-measurable-acceptance-and-release-gates)

The comparison is based on published source, model files, and documentation. RAFIQ browser performance and detection accuracy still need measurement.
