# minirack-2020

3D model for a **minirack (10" width)** with **adjustable height and depth**. The frame is built with **2020 extrusion**, **Slot 5** (5 mm slot / M5-compatible). The model and cut list are generated with [Build123d](https://github.com/gumyr/build123d) (programmatic CAD).

Hole-to-hole width: 9.312" or 236.525 mm, see [geerlingguy/mini-rack](https://github.com/geerlingguy/mini-rack) for more details.

## Setup

Requires Python 3.10+ and [uv](https://github.com/astral-sh/uv).

```bash
uv venv -p 3.12
uv sync
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### VS Code viewer

- Select the `.venv` interpreter (e.g. **Python: Select Interpreter**).
- Install recommended extensions when prompted (includes the build123d viewer: **OCP CAD Viewer**).
