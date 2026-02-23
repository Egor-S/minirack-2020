# ruff: noqa: F403, F405
# %%
from build123d import *
from ocp_vscode import *

from lib import Profile2020I5

# %%
show(Profile2020I5(10 * MM), reset_camera=Camera.RESET)

# %%
