"""Project Phoebe - Fusion 360 entry point."""

import traceback

import adsk.core
import adsk.fusion


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

        root = design.rootComponent

        ui.messageBox(
            f"Project Phoebe initialized successfully!\n\n"
            f"Document : {app.activeDocument.name}\n"
            f"Root Component : {root.name}"
        )

    except Exception:
        if ui:
            ui.messageBox(traceback.format_exc())