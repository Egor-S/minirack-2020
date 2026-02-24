# minirack-2020

3D model for a **minirack (10" width)** with **adjustable height and depth**. The frame is built with **2020 extrusion**, **Slot 5** (5 mm slot / M5-compatible). The model and cut list are generated with [Build123d](https://github.com/gumyr/build123d) (programmatic CAD).

Hole-to-hole width: 9.312" or 236.525 mm, see [geerlingguy/mini-rack](https://github.com/geerlingguy/mini-rack) for more details.

## Bill of materials

| Name                | Count   | Description                                    |
| ------------------- | ------- | ---------------------------------------------- |
| Profile `216.52 mm` | 4       | Left-to-right, ±mm should be fine              |
| Profile `D - 40 mm` | 4       | Front-to-back, `D` is outer depth of the rack  |
| Profile `H mm`      | 4       | Bottom-to-top, `H` is outer height of the rack |
| DIN 7380 M5x12mm    | 16      | For blind joints, buttonhead                   |
| DIN 7380 M5x6mm     | `U * 4` | For mounting hardware                          |
| T-Nut M5            | `U * 4` | For mounting hardware, spring is handy         |

> Rack height for `U` rack units is `H = U * 44.45 mm + 40 mm`. 400 mm is perfect for 8U

The rack is designed for Aluminum profile extrusion 2020, I-type, Slot 5. You can buy it in Europe from:

- [Motedis](https://www.motedis.com/en/Aluminium-Profile-20x20-I-Typ-slot-5)
- [DOLD Mechatronik](https://www.dold-mechatronik.de/Aluminum-profile-20x20-I-type-groove-5)
- Amazon

## Assembly

Tools needed:

- M5 tap
- M5 allen key with a long thin bit
- Drill bit that is slightly larger than the allen key
- Oil/grease/WD-40 for tapping and drilling

Instructions:

1. Tap threads from both ends of all left-to-right and front-to-back profiles. Use oil/grease/WD-40
2. Screw M5 screws to tapped holed
3. Drill holes on both ends of all bottom-to-top profiles for blind joints: 10 mm from the end, from all 4 sides (2 pass-through holes)
4. Assemble front and back frames
5. Assemble the rack

## Build123d setup

Requires Python 3.10+ and [uv](https://github.com/astral-sh/uv).

```bash
uv venv -p 3.12
uv sync
source .venv/bin/activate
```

### VS Code viewer

- Select the `.venv` interpreter (e.g. **Python: Select Interpreter**).
- Install recommended extensions when prompted (includes the build123d viewer: **OCP CAD Viewer**).
