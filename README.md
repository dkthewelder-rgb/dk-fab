# dk-fab
AI-driven manufacturing geometry language for SolidWorks
# DK FAB AI MANUAL (VERSION 1)

## What DK Fab Is

DK Fab is a **manufacturing geometry language**.

DK Fab is NOT:
- CAD software
- Engineering software
- A parametric modeller

DK Fab DOES:
- Receive simple geometry
- Pass it to SolidWorks
- Create real parts

The AI performs ALL engineering.

DK Fab only draws geometry.

---

## Core Principle

**Convert engineering → geometry → DK Fab**

The AI must:
1. Understand the part
2. Reduce it to geometry
3. Output DK Fab commands

DK Fab does NOT understand:
- sprockets
- motors
- bearings
- brackets
- gears

It only understands geometry.

---

## Supported Commands

### Structure

PART name=<name>

PLATE width=<mm> height=<mm> thickness=<mm>

PROFILE outer
END_PROFILE

SKETCH operation=cut
END_SKETCH

SAVE name=<name>

---

### Geometry

LINE x1=<mm> y1=<mm> x2=<mm> y2=<mm>

CIRCLE x=<mm> y=<mm> diameter=<mm>

ARC x=<mm> y=<mm> radius=<mm> start=<deg> end=<deg>

SLOT x=<mm> y=<mm> length=<mm> width=<mm> angle=<deg>

---

## Units

All dimensions are in millimetres.

---

## Coordinate System

0,0 is centre of the part

+X = right  
-X = left  

+Y = up  
-Y = down  

---

## SolidWorks Rules (CRITICAL)

- Only ONE sketch is used
- Outer profile must be a CLOSED loop
- Internal shapes are drawn in the SAME sketch
- Boss Extrude is used once
- Internal closed loops automatically become holes
- DO NOT use cut-extrude
- DO NOT create multiple sketches

---

## Geometry Rules

- All outer profiles MUST be closed
- No gaps between lines
- No overlapping lines
- Arcs must connect cleanly to lines
- Prefer ARC over many small LINE segments
- Use SLOT instead of manually drawing slots
- Keep geometry clean and simple

---

## How the AI Should Think

DO NOT think in CAD commands.

Think in manufacturing geometry.

Every part is made from:

- Lines
- Arcs
- Circles
- Slots

Ignore the name of the object.

Convert:

"bracket" → geometry  
"sprocket" → geometry  
"gear" → geometry  

The AI performs abstraction.

DK Fab performs construction.

---

## Workflow

User request:
"Make a plate with 4 holes"

AI thinking:
- Plate size
- Hole positions
- Geometry layout

AI output:
DK Fab code

DK Fab:
→ sends to SolidWorks  
→ creates part  

---

## Example

### Input
"100x100 plate with 4 holes"

### Output

PART name=plate

PLATE width=100 height=100 thickness=6

SKETCH operation=cut

CIRCLE x=30 y=30 diameter=10
CIRCLE x=-30 y=30 diameter=10
CIRCLE x=30 y=-30 diameter=10
CIRCLE x=-30 y=-30 diameter=10

END_SKETCH

SAVE name=plate

---

## Important Rule

DK Fab must remain SIMPLE.

Never add complex engineering concepts into DK Fab.

All intelligence must remain in the AI.

---

## Goal

Allow ANY LLM to:

- Understand a real-world part
- Convert it into geometry
- Output DK Fab code
- Create a manufacturable CAD model

---

## Final Principle

**DK Fab is a language for communicating manufacturing geometry from an intelligent system to a CAD system.**
