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

---

# Construction Material

Revision: November 8, 2026 — full-width cedar construction, two roofs, side mounting, and replaceable entrance plate.

Primary material:

- Untreated solid Western Red Cedar, smooth on the exterior face.
- Design thickness: **20.6375 mm (13/16 inch) provisional**, replacing the original 5 mm plywood.
- Selected stock format: nominal 1 × 6 cedar, provisionally 5.5 inches (139.7 mm) wide.
- No rip cuts or edge-glued panels. Use full board widths, crosscuts, angled crosscuts, drilling, and laser engraving.
- Measure the purchased board and set the material-thickness parameter to its actual thickness before generating final dimensions or cutting parts.
- Use this thickness for the walls, structural front, back, floor, and structural roof. Decorative roof thickness remains a separate parameter.
- Cut structural panels with woodworking saws; use the Monport laser for exterior front engraving.

Finish:

- Optional exterior-grade finish on exterior surfaces only; leave the nesting interior unfinished
- Decorative roof material and color remain to be selected
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

# Roof System

Two separate roofs, with an isolated ESP32-CAM compartment between them.

## Hidden Interior Roof

- Flat cedar ceiling closing the nesting cavity; not visible from outside.
- Fits between the walls, using full-width 1 × 6 stock crosscut to length, like the floor.
- Separates the birds from camera electronics; camera viewing opening and mounting details remain to be designed.
- Thickness follows the structural cedar parameter.
- Assembly clearances and attachment must accommodate wood movement without requiring rip cuts.

## Visible Decorative Roof

- Single sloped roof, approximately 10–15°; not a traditional peaked roof.
- Sheds rain and covers the camera compartment.
- Material undecided: possible 3D-printed plastic, acrylic, or another suitable outdoor material.
- Material thickness, weather resistance, fastening, and water-shedding details require validation after material selection.
- Removable for camera maintenance, using discreet accessible fasteners.
- Rounded corners; provisional corner radius 10–15 mm.
- Compact overhangs rather than the original large roof: provisional front 20 mm, sides 10–15 mm, rear essentially flush.
- Final overhangs remain subject to appearance and rain protection review in CAD.
- Keep the rear clear of the post and mounting hardware.
- Preserve clearance for the upward-sliding cleaning panel; check whether roof removal is needed for full panel withdrawal.

---

# Front

Solid cedar structural front with the smooth face outward for direct laser engraving.

A second decorative front layer is optional rather than required to hide finger joints. Final facade detailing remains to be selected.

Advantages:

- Premium appearance
- Hidden joints
- Decorative engraving possible
- Better weather resistance

---

# Entrance Hole and Replaceable Plate

- Entrance diameter: 28.575 mm (1⅛ inch), displayed as 28.6 mm.
- Drill the full entrance through the cedar front; the plate does not replace the structural wood.
- Position above the nesting floor at a species-appropriate height; final height remains to be set.
- No perch.

Decorative entrance plate:

- Laser-cut from the user's existing 3 mm acrylic.
- Matching entrance opening, aligned with the cedar hole; smooth the opening edges.
- Shape and color can coordinate with the visible roof; final outline remains undecided.
- Attach with two decorative brass screws, using clearance holes in the acrylic and pilot holes in the cedar.
- Keep screw tips out of the nesting cavity. Tighten gently; avoid clamping stresses that crack the acrylic.
- No permanent adhesive: plate must be removable and replaceable if damaged.
- Treat as decorative trim with limited protection, not a squirrel-proof guard. Acrylic can crack or be chewed; it is not equivalent to metal.

---

# Interior

Floor:

Full-width 1 × 6 construction replaces the original approximately square cavity.

With board width W = 139.7 mm and thickness T = 20.6375 mm:

| Dimension | Formula | Provisional size |
|---|---|---|
| Internal width | W − 2T | 98.425 mm (3⅞ inches) |
| Internal depth | W | 139.7 mm (5½ inches) |
| Exterior body width | W | 139.7 mm |
| Exterior body depth | W + 2T | 180.975 mm (7⅛ inches) |

Front and back overlap the side edges. All wall panels retain the full stock width.
Orient the floor and hidden roof with stock width along the house depth; crosscut their length to fit the internal width.
These are geometric dimensions before assembly, drainage, and sliding-door clearances. Detail those clearances without introducing rip cuts.
Recalculate the cavity from measured stock dimensions and review suitability before finalizing the cut list.

Interior height:

Per chickadee recommendations.

Include:

- Rough climbing surface beneath entrance
- Ventilation near roof
- Drainage holes in floor

---

# Mounting and Placement

- Attach the back of the house to the SIDE of a 4 × 4 post, not the top.
- Typical post width is 88.9 mm (3½ inches); measure before finalizing hardware.
- Center the approximately 139.7 mm-wide body on the post: approximately 25.4 mm extension on each side.
- Body projects approximately 180.975 mm forward from its rear face, plus any mounting-bracket offset and front roof overhang.
- Keep mounting offset and roof overhangs modest.
- Prioritize easy installation: proposed separate bracket fixed to the post first, then hang the house and secure it against lifting or rocking with accessible retaining screws.
- Final bracket geometry is undecided; keep fasteners discreet and independent of cleaning access, camera access, and drainage.
- Use stainless steel structural mounting screws.
- No post baffle, per owner preference. Squirrels can threaten eggs and nestlings; the acrylic entrance plate does not eliminate that risk.

Placement guidance discussed (not a confirmed installation location):

- Black-capped Chickadee nest-box height guidance: 5–15 feet above ground.
- Practical starting point: approximately 6 feet to the nesting floor for maintenance access.
- Prefer an east or southeast entrance if sheltered from local prevailing wind and driving rain.
- Favor partial sunlight, morning sun and afternoon shade, near mature trees with an unobstructed approach.
- Local shelter and exposure take priority over a fixed compass direction.
- Reference: Cornell NestWatch placement guidance, https://nestwatch.org/learn/all-about-birdhouses/nest-box-placement/

---

# Clean-out Door

Chosen design:

Right side panel

Slides upward.

Advantages:

- Hidden
- Weather resistant
- Sized for solid cedar, with sliding clearance adjusted for seasonal movement
- No hinges
- Easy cleaning

Retention:

Single brass screw near top.

---

# Joinery

Primary goal:

Use concealed pocket-hole screws and exterior-rated waterproof wood glue for permanent wall joints.

Finger joints are no longer part of this cedar construction.

Select pocket-hole settings and screw length for the measured board thickness; verify on scrap cedar before assembly. Use screws suitable for outdoor cedar exposure.

Do not glue the sliding clean-out panel. Detail the floor and roof attachments to allow drainage, maintenance, and seasonal wood movement.

Exterior should appear clean and minimal.

---

# Hardware

Minimal hardware.

Preferred:

- Brass screw for sliding panel
- Two decorative brass screws for the replaceable acrylic entrance plate
- Stainless steel mounting screws
- Exterior-suitable pocket-hole screws for fixed structural joints

No visible hinges.

---

# Finish

Natural wood body.

Decorative roof color and material to be selected; coordinate with the acrylic entrance plate.

Possible future options:

- Engraved chickadee
- Family name
- House number

---

# CAD Philosophy

Everything should be parametric.

Nothing should use hard-coded dimensions.

Changing one parameter should automatically regenerate the design.

---

# Initial Parameters

Material

- Structural cedar thickness: 20.6375 mm (13/16 inch) provisional; replace with measured board thickness
- Stock width: 139.7 mm provisional; replace with measured width
- Acrylic entrance plate thickness: 3 mm
- Decorative roof thickness: separate parameter, to be confirmed
- Joint and sliding clearances
- Laser kerf: optional for future laser-cut decorative parts; not used to size saw-cut structural panels

House

- Interior cavity width
- Interior cavity depth
- Interior cavity height
- Derive cavity and exterior dimensions from measured stock width, thickness, and overlapping butt-joint arrangement.
- Preserve the no-rip/no-edge-gluing constraint; flag stock changes that make cavity dimensions unsuitable.
- Interior height remains independently adjustable.

Roof

- Pitch
- Front overhang
- Side overhang
- Rear overhang
- Corner radius

Entrance

- Diameter: 28.575 mm
- Height above nesting floor
- Plate outline, thickness, screw spacing, and screw clearance

Ventilation

- Slot width
- Slot count

Sliding Door

- Clearance
- Rail width
- Rail depth

Mounting

- Post size
- Mounting hole spacing
- Bracket offset and retaining-screw access

---

# Software Architecture

Project Structure

BirdHouse/

    README.md

    src/

        main.py

        parameters.py

        geometry.py

        material.py

        roof.py

        front.py

        back.py

        left_wall.py

        right_wall.py

        floor.py

        joints.py

        assembly.py

        export.py

---

# Object Model

Material

Responsible for:

- Measured structural thickness
- Separate thicknesses for decorative parts
- Joint clearances
- Optional kerf calculations for laser-cut accessories; no press-fit finger joints in the cedar structure

Roof

Responsible for:

- Hidden cedar ceiling and separate sloped outer roof geometry
- Camera-compartment clearance and service access
- Overhang
- Corner radius

Wall

Responsible for:

- Basic wall geometry

FrontWall

Adds:

- Entrance hole
- Replaceable acrylic plate and brass screw locations
- Exterior engraving area

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

Develop geometry utilities.

Examples:

draw_rectangle()

draw_circle()

rounded_rectangle()

center_rectangle()

offset_profile()

Phase 4

Generate the floor.

Phase 5

Generate walls.

Phase 6

Generate the hidden cedar roof, camera compartment, and separate removable sloped outer roof.

Phase 7

Generate butt-joint assembly geometry and concealed pocket-screw locations for the cedar construction.

Phase 8

Assemble complete birdhouse.

Phase 9

Export engraving artwork/templates as SVG/DXF and generate dimensioned panel drawings or a cut list for saw cutting.

Phase 10

Prototype cedar joinery on scrap, saw-cut the panels, test laser engraving on a cedar offcut, then assemble the birdhouse.

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
