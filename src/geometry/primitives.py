import adsk.core


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