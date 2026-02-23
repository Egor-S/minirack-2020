import build123d as bd

from .common import profiles_dir


profile = bd.import_step(profiles_dir / "Motedis_Profile_20x20_I-Type_slot_5.stp")
face = profile.faces_intersected_by_axis(bd.Axis.Z)[0]


class Profile2020I5(bd.Part):
    def __init__(
        self,
        length: float,
    ):
        with bd.BuildPart() as component:
            bd.extrude(face, length)
        super().__init__(obj=component.part)
