"""Project Phoebe - Fusion 360 entry point."""

import traceback
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import adsk.core
import adsk.fusion
import math

# Dimensions in millimeters.
BOARD_WIDTH_MM = 139.7
MATERIAL_THICKNESS_MM = 20.6375

INTERIOR_WIDTH_MM = BOARD_WIDTH_MM - 2 * MATERIAL_THICKNESS_MM
INTERIOR_DEPTH_MM = BOARD_WIDTH_MM

WALL_HEIGHT_MM = 220.0  # Temporary overall height from floor underside.

ENTRANCE_DIAMETER_MM = 28.575
ENTRANCE_CENTER_ABOVE_FLOOR_MM = 150.0

ENTRANCE_PLATE_WIDTH_MM = 50.0
ENTRANCE_PLATE_HEIGHT_MM = 50.0
ENTRANCE_PLATE_THICKNESS_MM = 3.0

ROOF_SLOPE_DEG = 12.0
ROOF_THICKNESS_MM = 5.0
ROOF_SIDE_OVERHANG_MM = 20.0
ROOF_FRONT_OVERHANG_MM = 30.0
ROOF_REAR_OVERHANG_MM = 0.0
ROOF_FRONT_CORNER_RADIUS_MM = 12.0

CAMERA_CLEARANCE_FRONT_MM = 30.0


def run(_context):
    """Entry point called by Fusion 360."""
    ui = None

    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox(
                "Please open or create a Fusion Design before running Phoebe."
            )
            return

        helper_path = (
            Path(__file__).resolve().parents[1]
            / "src" / "geometry" / "primitives.py"
        )
        spec = spec_from_file_location("phoebe_primitives", helper_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load Phoebe's helper at {helper_path}")

        primitives = module_from_spec(spec)
        spec.loader.exec_module(primitives)
        create_panel = primitives.create_panel
        cut_entrance_hole = primitives.cut_entrance_hole

        root = design.rootComponent

        # Remove previous Phoebe test geometry.
        for occurrence in list(root.occurrences):
            if occurrence.component.name in (
                "Floor", "Left Wall", "Right Wall",
                "Back", "Front", "Interior Roof", "Entrance Plate", "Outer Roof"
            ):
                occurrence.deleteMe()

        floor = create_panel(
            parent=root,
            name="Floor",
            width_mm=INTERIOR_WIDTH_MM,
            depth_mm=INTERIOR_DEPTH_MM,
            height_mm=MATERIAL_THICKNESS_MM,
        )

        # Distance from the assembly center to each wall's center.
        side_offset_mm = (
            INTERIOR_WIDTH_MM / 2 + MATERIAL_THICKNESS_MM / 2
        )
        end_offset_mm = (
            INTERIOR_DEPTH_MM / 2 + MATERIAL_THICKNESS_MM / 2
        )

        left_wall = create_panel(
            parent=root,
            name="Left Wall",
            width_mm=MATERIAL_THICKNESS_MM,
            depth_mm=INTERIOR_DEPTH_MM,
            height_mm=WALL_HEIGHT_MM,
            x_mm=-side_offset_mm,
        )

        right_wall = create_panel(
            parent=root,
            name="Right Wall",
            width_mm=MATERIAL_THICKNESS_MM,
            depth_mm=INTERIOR_DEPTH_MM,
            height_mm=WALL_HEIGHT_MM,
            x_mm=side_offset_mm,
        )

        back = create_panel(
            parent=root,
            name="Back",
            width_mm=BOARD_WIDTH_MM,
            depth_mm=MATERIAL_THICKNESS_MM,
            height_mm=WALL_HEIGHT_MM,
            y_mm=end_offset_mm,
        )

        front = create_panel(
            parent=root,
            name="Front",
            width_mm=BOARD_WIDTH_MM,
            depth_mm=MATERIAL_THICKNESS_MM,
            height_mm=WALL_HEIGHT_MM,
            y_mm=-end_offset_mm,
        )

        cut_entrance_hole(
            component=front,
            diameter_mm=ENTRANCE_DIAMETER_MM,
            center_z_mm=(
                MATERIAL_THICKNESS_MM + ENTRANCE_CENTER_ABOVE_FLOOR_MM
            ),
            thickness_mm=MATERIAL_THICKNESS_MM,
        )

        interior_roof = create_panel(
            parent=root,
            name="Interior Roof",
            width_mm=INTERIOR_WIDTH_MM,
            depth_mm=INTERIOR_DEPTH_MM,
            height_mm=MATERIAL_THICKNESS_MM,
            z_mm=WALL_HEIGHT_MM - MATERIAL_THICKNESS_MM,
        )

        entrance_center_z_mm = (
            MATERIAL_THICKNESS_MM + ENTRANCE_CENTER_ABOVE_FLOOR_MM
        )

        # Outside the front panel, toward negative Y.
        plate_center_y_mm = -(
            INTERIOR_DEPTH_MM / 2
            + MATERIAL_THICKNESS_MM
            + ENTRANCE_PLATE_THICKNESS_MM / 2
        )

        entrance_plate = create_panel(
            parent=root,
            name="Entrance Plate",
            width_mm=ENTRANCE_PLATE_WIDTH_MM,
            depth_mm=ENTRANCE_PLATE_THICKNESS_MM,
            height_mm=ENTRANCE_PLATE_HEIGHT_MM,
            y_mm=plate_center_y_mm,
            z_mm=entrance_center_z_mm - ENTRANCE_PLATE_HEIGHT_MM / 2,
        )

        cut_entrance_hole(
            component=entrance_plate,
            diameter_mm=ENTRANCE_DIAMETER_MM,
            center_z_mm=ENTRANCE_PLATE_HEIGHT_MM / 2,
            thickness_mm=ENTRANCE_PLATE_THICKNESS_MM,
        )

        roof_angle = math.radians(ROOF_SLOPE_DEG)

        body_depth_mm = (
            INTERIOR_DEPTH_MM + 2 * MATERIAL_THICKNESS_MM
        )

        roof_width_mm = (
            BOARD_WIDTH_MM + 2 * ROOF_SIDE_OVERHANG_MM
        )

        # Horizontal coverage, viewed from above.
        roof_run_mm = (
            body_depth_mm
            + ROOF_FRONT_OVERHANG_MM
            + ROOF_REAR_OVERHANG_MM
        )

        # Actual panel length must account for its slope.
        roof_length_mm = roof_run_mm / math.cos(roof_angle)

        roof_center_y_mm = (
            ROOF_REAR_OVERHANG_MM - ROOF_FRONT_OVERHANG_MM
        ) / 2

        front_wall_y_mm = -body_depth_mm / 2

        # Height of the roof underside at its center.
        roof_center_z_mm = (
            WALL_HEIGHT_MM
            + CAMERA_CLEARANCE_FRONT_MM
            + (roof_center_y_mm - front_wall_y_mm)
            * math.tan(roof_angle)
        )

        outer_roof = create_panel(
            parent=root,
            name="Outer Roof",
            width_mm=roof_width_mm,
            depth_mm=roof_length_mm,
            height_mm=ROOF_THICKNESS_MM,
            y_mm=roof_center_y_mm,
            z_mm=roof_center_z_mm,
            rotation_x_deg=ROOF_SLOPE_DEG,
            front_corner_radius_mm=ROOF_FRONT_CORNER_RADIUS_MM
        )

        ui.messageBox(
            "Birdhouse body, entrance plate, and both roofs "
            "created successfully.\n"
            f"Outer roof slope: {ROOF_SLOPE_DEG:.1f} degrees."
        )

    except Exception:
        if ui is None:
            raise
        ui.messageBox(traceback.format_exc())