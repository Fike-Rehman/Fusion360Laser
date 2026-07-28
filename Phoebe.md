# Project Phoebe

### Parametric Fusion 360 / Python Project

---

# Project Vision

Design and generate a premium-quality chickadee birdhouse using Python and the Autodesk Fusion 360 API.

The project has two equally important goals:

1. Learn Python
2. Learn parametric CAD programming using Fusion 360

Rather than simply designing a birdhouse, we will build a reusable CAD framework capable of generating many laser-cut projects in the future.

---

# Design Philosophy

The birdhouse should NOT look like a typical laser-cut kit.

Instead it should resemble a professionally designed piece of outdoor architecture.

Design priorities:

- Clean
- Modern
- Minimal
- Functional
- Durable
- Easy to maintain
- Easy to manufacture
- Future expandable

---

# Construction Material

Primary material:

- 5 mm Baltic Birch plywood

Finish:

- Exterior-grade finish
- Decorative roof painted for contrast
- Natural wood body

---

# Species

Black-capped Chickadee

Follow accepted nesting recommendations for:

- Interior floor size
- Entrance diameter
- Entrance height
- Ventilation
- Drainage

The design may eventually support additional bird species.

---

# Roof Assembly

The roof is a multi-layer assembly.

From top to bottom:

1. Decorative sloped roof
2. Hidden electronics cavity
3. Structural flat roof
4. Birdhouse walls
5. Floor

The structural roof serves as the ceiling of the nesting chamber.

The decorative roof provides:

- Weather protection
- Premium appearance
- Hidden joinery
- Space for future electronics

---

# Roof

Style:

Single sloped roof

NOT:

- Flat roof
- Traditional peaked roof

Characteristics:

- Modern appearance
- Approximately 10–15° slope (adjustable as required for electronics cavity)
- Large front overhang
- Side overhangs
- Minimal rear overhang

Roof overhang:

Front:
35–40 mm

Sides:
20–25 mm

Rear:
0–10 mm

---

# Decorative Roof

Purpose:

- Premium appearance
- Hide structural joints
- Increase weather protection
- Painted contrasting color

Features:

- Rounded corners
- Small reveal around structural roof
- Approximately 10–15 mm corner radius

The decorative roof should be removable for servicing the electronics cavity.

---

# Electronics Cavity

The birdhouse shall be designed from the beginning to accommodate future electronics while maintaining proper nesting dimensions.

Initial design target:

- ESP32-CAM module

Future possibilities:

- Temperature sensor
- Humidity sensor
- Microphone
- LED illumination
- Battery pack
- Solar charging
- Additional sensors

Requirements:

- Completely hidden from outside
- Isolated from nesting chamber
- Accessible through service hatch
- No exposed wiring
- Ventilated
- Weather resistant

---

# Electronics Service Hatch

The decorative roof shall include a concealed service hatch allowing access to the electronics cavity.

Purpose:

- Install or replace ESP32-CAM
- Replace SD card
- Route wiring
- Perform maintenance

Requirements:

- Hidden from normal view
- Weather resistant
- Easily removable
- Does not require opening the nesting chamber

---

# Camera Support

Reserve space for an optional camera.

Preferred camera location:

- Mounted within the electronics cavity
- Looking downward into the nesting chamber

Goals:

- Entire nest visible
- Camera completely hidden
- No visible external modifications
- No perch required

---

# Front

Double-layer construction.

Structural front

Decorative front

Advantages:

- Premium appearance
- Hidden joints
- Decorative engraving
- Better weather resistance

---

# Entrance Hole

Approximately:

32 mm diameter

Placement:

Centered visually while maintaining recommended height above floor.

No perch.

---

# Interior

Floor:

100–110 mm square

Interior height:

Follow chickadee recommendations.

Include:

- Rough climbing surface beneath entrance
- Ventilation near roof
- Drainage holes in floor

The structural roof forms the ceiling of the nesting chamber.

---

# Mounting

Designed specifically for mounting on a 4×4 post.

Back panel:

- Large mounting area
- Hidden screw locations
- Stainless steel mounting screws

Minimal rear roof overhang allows flush mounting.

---

# Clean-out Door

Chosen design:

Right side panel

Slides upward.

Advantages:

- Hidden
- Weather resistant
- Laser-cut friendly
- No hinges
- Easy cleaning

Retention:

Single brass screw near top.

---

# Joinery

Primary goal:

Hide visible finger joints whenever practical.

Structural finger joints are acceptable if hidden behind decorative panels.

Exterior should appear clean and minimal.

---

# Hardware

Minimal hardware.

Preferred:

- Brass retaining screw
- Stainless steel mounting screws

No visible hinges.

---

# Finish

Natural wood body.

Painted decorative roof.

Possible future options:

- Engraved chickadee
- Family name
- House number

---

# CAD Philosophy

Everything shall be parametric.

Nothing shall use hard-coded dimensions.

Changing one parameter should automatically regenerate the design.

---

# Initial Parameters

## Material

- Thickness
- Kerf
- Glue clearance

## House

- Width
- Depth
- Height

## Roof

- Pitch
- Front overhang
- Side overhang
- Rear overhang
- Corner radius

## Entrance

- Diameter
- Height

## Ventilation

- Slot width
- Slot count

## Sliding Door

- Clearance
- Rail width
- Rail depth

## Mounting

- Post size
- Mounting hole spacing

## Electronics

- Enabled
- Cavity height
- Cavity width
- Cavity depth
- Camera opening
- Camera offset
- Service hatch size
- Wire channel width
- Ventilation openings

---

# Software Architecture

BirdHouse/

    README.md

    src/

        main.py

        parameters.py

        geometry.py

        material.py

        panel.py
        front.py
        back.py
        left_wall.py
        right_wall.py
        floor.py

        roof.py
        electronics.py

        joints.py
        assembly.py
        export.py

---

# Object Model

Material

Responsible for:

- Thickness
- Kerf
- Press-fit calculations

Panel

Base class responsible for:

- Sketch creation
- Extrusion
- Common geometry
- Joint interfaces

Roof

Responsible for:

- Structural roof
- Decorative roof
- Roof cavity
- Overhangs
- Corner radius

Electronics

Responsible for:

- Electronics cavity
- Camera mounting
- Service hatch
- Wire routing

FrontWall

Adds:

- Entrance hole
- Decorative front

SlidingWall

Adds:

- Sliding rails
- Retaining screw

BirdHouse

Responsible for assembling all components.

---

# Development Plan

Phase 1

Learn Python

- Classes
- Dataclasses
- Methods
- Properties
- Composition

Phase 2

Learn Fusion API

- Components
- Sketches
- Parameters
- Extrusions

Phase 3

Develop reusable geometry utilities.

Phase 4

Generate floor.

Phase 5

Develop generic panel class.

Phase 6

Generate walls.

Phase 7

Generate roof assembly.

Phase 8

Generate electronics cavity.

Phase 9

Generate joinery.

Phase 10

Assemble birdhouse.

Phase 11

Export SVG/DXF.

Phase 12

Prototype on laser cutter.

---

# Future Goals

The birdhouse is only the first application.

Eventually the framework should generate:

- Birdhouses
- Boxes
- Edge-lit sign bases
- Model railroad buildings
- Drawer organizers
- Tool holders
- Electronics enclosures

The long-term goal is to create a reusable parametric CAD framework rather than a collection of one-off scripts.
