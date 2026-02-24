import build123d as bd

from .common import profiles_dir


profile = bd.import_step(profiles_dir / "Motedis_Profile_20x20_I-Type_slot_5.stp")
face = profile.faces_intersected_by_axis(bd.Axis.Z)[1]  # facing up
face.locate(bd.Location(-face.center()))  # move to origin


class Profile2020I5(bd.BasePartObject):
    """
    Aluminum extrusion 2020 I-Type slot 5 profile.

    Cross-section 20x20 mm, slot width 5 mm, center hole diameter 4.3 mm.
    """

    def __init__(
        self,
        length: float,
        rotation: bd.RotationLike = (0, 0, 0),
        **kwargs,
    ):
        """Create a 2020 I-Type slot 5 profile with the specified length."""
        with bd.BuildPart() as component:
            bd.extrude(face, length)
        super().__init__(part=component.part, rotation=rotation, **kwargs)
