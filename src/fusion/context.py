"""
Project Phoebe
==============

Fusion 360 context objects.

Author: Fike Rehman
Version: 0.1.0
"""

import adsk.core
import adsk.fusion


class FusionContext:
    """Provides convenient access to the main Fusion 360 objects."""

    def __init__(self):

        self.app = adsk.core.Application.get()
        self.ui = self.app.userInterface
        self.design = adsk.fusion.Design.cast(self.app.activeProduct)

        if self.design:
            self.root_component = self.design.rootComponent
        else:
            self.root_component = None