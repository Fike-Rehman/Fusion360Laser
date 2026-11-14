import adsk.core
import adsk.fusion
import math


def draw_center_rectangle(sketch, width_mm, height_mm):
    """
    Draw a rectangle centered at the sketch origin.

    Parameters:
        sketch: Fusion 360 Sketch object.
        width_mm: Rectangle width in millimeters.
        height_mm: Rectangle height in millimeters.
    """

    # Fusion's internal length unit is centimeters.
    half_width = width_mm / 20.0
    half_height = height_mm / 20.0

    bottom_left = adsk.core.Point3D.create(
        -half_width, -half_height, 0
    )

    top_right = adsk.core.Point3D.create(
        half_width, half_height, 0
    )

    lines = sketch.sketchCurves.sketchLines

    lines.addTwoPointRectangle(bottom_left, top_right)

def draw_front_rounded_rectangle(sketch, width_mm, depth_mm, radius_mm):
    """Draw a centered outline with all four corners rounded."""

    if not 0 < radius_mm < min(width_mm, depth_mm) / 2:
        raise ValueError("Corner radius is too large or must be positive.")

    half_width = width_mm / 20.0
    half_depth = depth_mm / 20.0
    radius = radius_mm / 10.0

    def point(x, y):
        return adsk.core.Point3D.create(x, y, 0)

    lines = sketch.sketchCurves.sketchLines
    arcs = sketch.sketchCurves.sketchArcs

    front_left = arcs.addByCenterStartSweep(
        point(-half_width + radius, -half_depth + radius),
        point(-half_width, -half_depth + radius),
        math.pi / 2,
    )

    front_right = arcs.addByCenterStartSweep(
        point(half_width - radius, -half_depth + radius),
        point(half_width - radius, -half_depth),
        math.pi / 2,
    )

    rear_right = arcs.addByCenterStartSweep(
        point(half_width - radius, half_depth - radius),
        point(half_width, half_depth - radius),
        math.pi / 2,
    )

    rear_left = arcs.addByCenterStartSweep(
        point(-half_width + radius, half_depth - radius),
        point(-half_width + radius, half_depth),
        math.pi / 2,
    )

    lines.addByTwoPoints(
        front_left.endSketchPoint, front_right.startSketchPoint
    )
    lines.addByTwoPoints(
        front_right.endSketchPoint, rear_right.startSketchPoint
    )
    lines.addByTwoPoints(
        rear_right.endSketchPoint, rear_left.startSketchPoint
    )
    lines.addByTwoPoints(
        rear_left.endSketchPoint, front_left.startSketchPoint
    )

def create_panel(
    parent,
    name,
    width_mm,
    depth_mm,
    height_mm,
    x_mm=0,
    y_mm=0,
    z_mm=0,
    rotation_x_deg=0,
    front_corner_radius_mm=0,
):
    """Create a rectangular panel component. All dimensions are in mm."""

    transform = adsk.core.Matrix3D.create()
    transform.setToRotation(
        math.radians(rotation_x_deg),
        adsk.core.Vector3D.create(1, 0, 0),
        adsk.core.Point3D.create(0, 0, 0),
    )
    transform.translation = adsk.core.Vector3D.create(
        x_mm / 10,
        y_mm / 10,
        z_mm / 10,
    )

    occurrence = parent.occurrences.addNewComponent(transform)
    component = occurrence.component
    component.name = name

    sketch = component.sketches.add(component.xYConstructionPlane)
    sketch.name = f"{name} Footprint"

    if front_corner_radius_mm > 0:
        draw_front_rounded_rectangle(
            sketch, width_mm, depth_mm, front_corner_radius_mm
        )
    else:
        draw_center_rectangle(sketch, width_mm, depth_mm)

    profile = sketch.profiles.item(0)
    extrusion = component.features.extrudeFeatures.addSimple(
        profile,
        adsk.core.ValueInput.createByString(f"{height_mm} mm"),
        adsk.fusion.FeatureOperations.NewBodyFeatureOperation,
    )

    if extrusion is None:
        raise RuntimeError(f"Fusion could not create {name}.")

    extrusion.name = f"{name} Extrusion"

    return component

def cut_entrance_hole(component, diameter_mm, center_z_mm, thickness_mm):
    """Cut through a panel centered on its local XZ plane."""

    sketch = component.sketches.add(component.xZConstructionPlane)
    sketch.name = "Entrance Hole Sketch"

    # Convert a point in component coordinates into sketch coordinates.
    center = sketch.modelToSketchSpace(
        adsk.core.Point3D.create(0, 0, center_z_mm / 10)
    )

    sketch.sketchCurves.sketchCircles.addByCenterRadius(
        center,
        diameter_mm / 20,  # Diameter in mm -> radius in cm.
    )

    extrudes = component.features.extrudeFeatures
    cut_input = extrudes.createInput(
        sketch.profiles.item(0),
        adsk.fusion.FeatureOperations.CutFeatureOperation,
    )

    # Cut both ways from the panel's midplane.
    # True means the distance is the total length across both directions.
    cut_input.setSymmetricExtent(
        adsk.core.ValueInput.createByString(f"{thickness_mm + 2} mm"),
        True,
    )

    # Restrict the cut to this panel's body.
    cut_input.participantBodies = [component.bRepBodies.item(0)]

    cut = extrudes.add(cut_input)
    if cut is None:
        raise RuntimeError("Fusion could not cut the entrance hole.")

    cut.name = "Entrance Hole Cut"
    sketch.isVisible = False

    return cut

