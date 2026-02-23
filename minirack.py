# ruff: noqa: F403, F405
# %%
from build123d import *
from ocp_vscode import *

from lib import Profile2020I5

dim = 20 * MM
mounts_distance = 236.525 * MM

height = 400 * MM
width = mounts_distance + dim
depth = 250 * MM + 2 * dim

# %%
vertical_profile = Profile2020I5(height)
facade_profile = (
    Pos(dim / 2, 0, dim / 2) * Rotation(0, 90, 0) * Profile2020I5(width - 2 * dim)
)
side_profile = (
    Pos(0, dim / 2, dim / 2) * Rotation(-90, 0, 0) * Profile2020I5(depth - 2 * dim)
)

assembly = Compound(
    children=[
        # vertical posts
        vertical_profile,
        Pos(width - dim, 0, 0) * vertical_profile,
        Pos(0, depth - dim, 0) * vertical_profile,
        Pos(width - dim, depth - dim, 0) * vertical_profile,
        # front and back cross beams
        facade_profile,
        Pos(0, 0, height - dim) * facade_profile,
        Pos(0, depth - dim, 0) * facade_profile,
        Pos(0, depth - dim, height - dim) * facade_profile,
        # side beams
        side_profile,
        Pos(0, 0, height - dim) * side_profile,
        Pos(width - dim, 0, 0) * side_profile,
        Pos(width - dim, 0, height - dim) * side_profile,
    ]
)
show(assembly, reset_camera=Camera.RESET)

# %%
