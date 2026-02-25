import argparse
from pathlib import Path

import build123d as bd

from minirack import build, dim, mounts_distance


def main():
    parser = argparse.ArgumentParser(description="Generate a 3D model of a mini rack.")
    parser.add_argument(
        "--height",
        type=float,
        default=400.0,
        help="Height of the mini rack in millimeters (default: 400 mm)",
    )
    parser.add_argument(
        "--depth",
        type=float,
        default=290.0,
        help="Depth of the mini rack in millimeters (default: 290 mm)",
    )
    parser.add_argument(
        "--drill-diameter",
        type=float,
        default=5.0,
        help="Diameter of the drill holes in millimeters (default: 5 mm)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("./export"),
        help="Output dir name for the generated STL model (default: ./export)",
    )

    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    rack = build(
        height=args.height, depth=args.depth, drill_diameter=args.drill_diameter
    )

    model_path: Path = args.output / "model.stl"
    bd.export_stl(rack, model_path)
    print(f"Mini rack model saved to {model_path}")

    bom_path: Path = args.output / "bom.csv"
    write_bom(height=args.height, depth=args.depth, path=bom_path)
    print(f"Bill of materials saved to {bom_path}")


def write_bom(height: float, depth: float, path: Path):
    units = int((height - 2 * dim) / 44.45)
    with open(path, "w") as f:
        f.write("Part,Length mm,Quantity\n")
        f.write(f"Profile,{round(mounts_distance - dim, 2)},4\n")
        f.write(f"Profile,{round(height, 2)},4\n")
        f.write(f"Profile,{round(depth - 2 * dim, 2)},4\n")
        f.write("DIN 7380 M5,12,16\n")
        f.write(f"DIN 7380 M5,6,{units * 4}\n")
        f.write(f"T-Nut M5,-,{units * 4}\n")


if __name__ == "__main__":
    main()
