
# %%
from pathlib import Path

from build123d import *
from ocp_vscode import *

root_dir = Path(__file__).parent.resolve()
profile = import_step(root_dir / "profiles/Motedis_Profile_20x20_I-Type_slot_5.stp")
face = profile.faces_intersected_by_axis(Axis.Z)[0]

# %%
show(extrude(face, 10 * MM), reset_camera=Camera.RESET)
