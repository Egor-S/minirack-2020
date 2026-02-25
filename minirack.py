# ruff: noqa: F403, F405
# %%
from build123d import *
from ocp_vscode import *

from lib import Profile2020I5

dim = 20 * MM
mounts_distance = 236.525 * MM
drill_diameter = 5 * MM

height = 400 * MM
width = mounts_distance + dim
depth = 250 * MM + 2 * dim

h = Vector(0, 0, height - dim)
w = Vector(width - dim, 0, 0)
d = Vector(0, depth - dim, 0)

# %%
with BuildPart() as rack:
    with Locations((0, 0, 0), w, d, w + d):
        Profile2020I5(height)
        with Locations((0, 0, dim / 2), (0, 0, height - dim / 2)):
            Cylinder(drill_diameter / 2, dim, rotation=(-90, 0, 0), mode=Mode.SUBTRACT)
            Cylinder(drill_diameter / 2, dim, rotation=(0, 90, 0), mode=Mode.SUBTRACT)

    b = Vector(dim / 2, 0, dim / 2)
    with Locations(b, h + b, d + b, h + d + b):
        Profile2020I5(width - 2 * dim, rotation=(0, 90, 0))

    b = Vector(0, dim / 2, dim / 2)
    with Locations(b, h + b, w + b, h + w + b):
        Profile2020I5(depth - 2 * dim, rotation=(-90, 0, 0))

show(rack.part, reset_camera=Camera.RESET)

# %%
