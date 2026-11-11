"""Project Phoebe - Fusion 360 entry point."""

import traceback
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import adsk.core
import adsk.fusion

# Dimensions in millimeters.
BOARD_WIDTH_MM = 139.7
MATERIAL_THICKNESS_MM = 20.6375

INTERIOR_WIDTH_MM = BOARD_WIDTH_MM - 2 * MATERIAL_THICKNESS_MM
INTERIOR_DEPTH_MM = BOARD_WIDTH_MM

WALL_HEIGHT_MM = 220.0  # Temporary overall height from floor underside.


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
        draw_center_rectangle = primitives.draw_center_rectangle

        root = design.rootComponent

        # Remove previous Phoebe test geometry.
        for occurrence in list(root.occurrences):
            if occurrence.component.name in ("Floor", "Left Wall", "Right Wall", "Back", "Front"):
                occurrence.deleteMe()

        occurrence = root.occurrences.addNewComponent(
            adsk.core.Matrix3D.create()
        )
        floor = occurrence.component
        floor.name = "Floor"

        floor_sketch = floor.sketches.add(floor.xYConstructionPlane)
        floor_sketch.name = "Floor Sketch"
        draw_center_rectangle(
            floor_sketch,
            INTERIOR_WIDTH_MM,
            INTERIOR_DEPTH_MM,
        )

        profile = floor_sketch.profiles.item(0)
        thickness = adsk.core.ValueInput.createByString(
            f"{MATERIAL_THICKNESS_MM} mm"
        )
        extrude = floor.features.extrudeFeatures.addSimple(
            profile,
            thickness,
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
        )
        if extrude is None:
            raise RuntimeError("Fusion could not create the floor extrusion.")

        extrude.name = "Floor Extrusion"

        # Position the wall beside the floor, along the negative X edge.
        wall_center_x_mm = -(
            INTERIOR_WIDTH_MM / 2 + MATERIAL_THICKNESS_MM / 2
        )

        wall_transform = adsk.core.Matrix3D.create()
        wall_transform.translation = adsk.core.Vector3D.create(
            wall_center_x_mm / 10,  # Fusion coordinates use centimeters.
            0,
            0,
        )

        wall_occurrence = root.occurrences.addNewComponent(wall_transform)
        left_wall = wall_occurrence.component
        left_wall.name = "Left Wall"

        # Draw the wall's narrow footprint, then extrude upward.
        wall_sketch = left_wall.sketches.add(left_wall.xYConstructionPlane)
        wall_sketch.name = "Left Wall Footprint"

        draw_center_rectangle(
            wall_sketch,
            MATERIAL_THICKNESS_MM,
            INTERIOR_DEPTH_MM,
        )

        wall_profile = wall_sketch.profiles.item(0)
        wall_extrude = left_wall.features.extrudeFeatures.addSimple(
            wall_profile,
            adsk.core.ValueInput.createByString(f"{WALL_HEIGHT_MM} mm"),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
        )

        if wall_extrude is None:
            raise RuntimeError("Fusion could not create the left wall.")

        wall_extrude.name = "Left Wall Extrusion"

        # Position the right wall beside the positive X edge.
        right_wall_center_x_mm = (
            INTERIOR_WIDTH_MM / 2 + MATERIAL_THICKNESS_MM / 2
        )

        right_wall_transform = adsk.core.Matrix3D.create()
        right_wall_transform.translation = adsk.core.Vector3D.create(
            right_wall_center_x_mm / 10,
            0,
            0,
        )

        right_wall_occurrence = root.occurrences.addNewComponent(
            right_wall_transform
        )
        right_wall = right_wall_occurrence.component
        right_wall.name = "Right Wall"

        right_wall_sketch = right_wall.sketches.add(
            right_wall.xYConstructionPlane
        )
        right_wall_sketch.name = "Right Wall Footprint"

        draw_center_rectangle(
            right_wall_sketch,
            MATERIAL_THICKNESS_MM,
            INTERIOR_DEPTH_MM,
        )

        right_wall_profile = right_wall_sketch.profiles.item(0)
        right_wall_extrude = right_wall.features.extrudeFeatures.addSimple(
            right_wall_profile,
            adsk.core.ValueInput.createByString(f"{WALL_HEIGHT_MM} mm"),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
        )

        if right_wall_extrude is None:
            raise RuntimeError("Fusion could not create the right wall.")

        right_wall_extrude.name = "Right Wall Extrusion"

        # Position the back beyond the rear edges of the side walls.
        back_center_y_mm = (
            INTERIOR_DEPTH_MM / 2 + MATERIAL_THICKNESS_MM / 2
        )

        back_transform = adsk.core.Matrix3D.create()
        back_transform.translation = adsk.core.Vector3D.create(
            0,
            back_center_y_mm / 10,
            0,
        )

        back_occurrence = root.occurrences.addNewComponent(back_transform)
        back = back_occurrence.component
        back.name = "Back"

        back_sketch = back.sketches.add(back.xYConstructionPlane)
        back_sketch.name = "Back Footprint"

        draw_center_rectangle(
            back_sketch,
            BOARD_WIDTH_MM,
            MATERIAL_THICKNESS_MM,
        )

        back_profile = back_sketch.profiles.item(0)
        back_extrude = back.features.extrudeFeatures.addSimple(
            back_profile,
            adsk.core.ValueInput.createByString(f"{WALL_HEIGHT_MM} mm"),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
        )

        if back_extrude is None:
            raise RuntimeError("Fusion could not create the back.")

        back_extrude.name = "Back Extrusion"

        # Position the front beyond the front edges of the side walls.
        front_center_y_mm = -(
            INTERIOR_DEPTH_MM / 2 + MATERIAL_THICKNESS_MM / 2
        )

        front_transform = adsk.core.Matrix3D.create()
        front_transform.translation = adsk.core.Vector3D.create(
            0,
            front_center_y_mm / 10,
            0,
        )

        front_occurrence = root.occurrences.addNewComponent(front_transform)
        front = front_occurrence.component
        front.name = "Front"

        front_sketch = front.sketches.add(front.xYConstructionPlane)
        front_sketch.name = "Front Footprint"

        draw_center_rectangle(
            front_sketch,
            BOARD_WIDTH_MM,
            MATERIAL_THICKNESS_MM,
        )

        front_profile = front_sketch.profiles.item(0)
        front_extrude = front.features.extrudeFeatures.addSimple(
            front_profile,
            adsk.core.ValueInput.createByString(f"{WALL_HEIGHT_MM} mm"),
            adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
        )

        if front_extrude is None:
            raise RuntimeError("Fusion could not create the front.")

        front_extrude.name = "Front Extrusion"

        ui.messageBox(
            f"Floor and four walls created successfully: "
            f"{INTERIOR_WIDTH_MM:.3f} x "
            f"{INTERIOR_DEPTH_MM:.3f} x "
            f"{MATERIAL_THICKNESS_MM:.3f} mm"
        )

    except Exception:
        if ui is None:
            raise
        ui.messageBox(traceback.format_exc())