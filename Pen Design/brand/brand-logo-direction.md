# RAFIQ brand logo direction

## Brand and audience

RAFIQ helps drivers and reviewers understand monitored driving sessions through local warnings, timelines, and reviewable evidence. The intended first impression is technical confidence. The wheel grounds the product in driving. The reverse face introduces the assistant through conversation.

## Research and visual inspiration

| Reference group | Design implication for RAFIQ |
| --- | --- |
| [Seeing Machines](https://seeingmachines.com/wp-content/uploads/2024/01/SEE-Event-Alert-CES-2024-FINAL2-03-01-24.pdf), [Smart Eye](https://www.smarteye.se/wp-content/uploads/2025/02/Smart-Eye-Year-End-Report-Q4-2024.pdf), [Cipia](https://mma.prnewswire.com/media/1361126/Cipia_Logo_v1.jpg) | Driver-monitoring identities make sensing an obvious visual theme. RAFIQ puts the driver's wheel in the foreground. |
| [Samsara](https://www.samsara.com/company/news/press-releases/samsara-brand-refresh-physical-ai), [Geotab](https://www.geotab.com/CMS-GeneralFiles-production/EMEA/Geotab_Trusted_data_insights-what_are_your_vehicles_telling_you.pdf), [KPIT](https://www.pentagram.com/work/kpit/story) | A technical identity must also work on a report. The static lockup carries the full name and stands on its own. |
| [Waze](https://www.pentagram.com/work/waze/story), [TomTom](https://www.tomtom.com/newsroom/behind-the-map/the-future-of-mapmaking-tomtom-orbis-maps/), [HERE](https://www.here.com/about/media-assets), [Waymo](https://waymo.com/media-resources/#logo) | A compact silhouette can carry a mobility brand into small touchpoints. Keep one recognizable outer rim across both faces. |
| [Lizzie by Ali Nazari](https://logosystem.co/logo/lizzie) | The user's motion reference supplied the idea of a circular reveal. RAFIQ uses original lettering, a three-spoke steering wheel, and a co-driver bot with a short antenna and two cyan eyes. |

## Three concepts explored

| Concept | Defining feature | Trade-off |
| --- | --- | --- |
| Straightaway | Symmetrical perspective road with a single centre dash, in cream and near-black | Simple at small sizes, with a possible letter A reading |
| Measured Road | A notch aligned with the dash links the roadway to a recorded moment, with a cyan accent | Strong link to evidence, though the notch loses prominence at favicon size |
| Apex | Asymmetric road, slight forward lean, and green accent | Energetic, with stronger motorsport associations |

## Approved final direction

The two-sided badge supersedes the road concepts. Place it to the right of an uppercase RAFIQ wordmark that writes on once over 1.2 seconds, then holds. The wheel is the first face and the static identity. The reverse shows the AI assistant. Use the combination in headers with enough room and the standalone wheel in tight headers and browser tabs.

| Time within the repeating loop | Action |
| --- | --- |
| 0.0–1.4 s | Hold the wheel facing forward |
| 1.4–2.0 s | Flip around the vertical axis, switching faces edge-on at 1.7 s |
| 2.0–3.4 s | Hold the co-driver bot facing forward |
| 3.4–4.0 s | Flip back, switching faces at 3.7 s |

## Colour, lettering, and construction

Use the [project palette](../../docs/DESIGN.md). The background is near-black `#0E100F`. The lettering, rim, wheel, and bot outline use warm cream `#FFFCE1`. Reserve cyan `#00BAE2` for the eyes. Keep the dark backing when placing this version on a light surface.

The prototype uses original vector lettering with broad proportions, an upright I, and a diagonal Q tail. The five letters are outlined paths. Product interface text continues to follow DESIGN.md. At the master size, the badge spans 92 units and the gap to the Q is 16 units. Scale the combination proportionally.

## Canva and website handoff

Open the [Canva prototype](https://www.canva.com/d/-CRXKOxcjZYo_5J). For a fresh Canva layout, upload `rafiq-loop.gif` and place it as a single animated element on the dark canvas. The GIF includes both holds, both flips, and the fixed lettering. Preserve its aspect ratio and original speed. Use `rafiq-static.svg` for a still composition and `rafiq-favicon.svg` for the wheel alone.

Open `rafiq-prototype.html` locally to review the one-time lettering introduction, continuous badge playback, the replay and pause controls, and the static version shown when the browser requests reduced motion. The self-contained prototype embeds its assets. The GIF encodes a four-second infinite loop. Canva import succeeded, but the connector did not expose a playable preview for checking playback after conversion.
