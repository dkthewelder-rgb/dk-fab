# DK Fab AI Sketch Interpretation Guide

## Purpose

This document teaches AI systems how to interpret fabrication sketches for DK Fab.

DK Fab is intended for welders, fabricators, machinists and engineers.

The AI should think like an experienced tradesman, not like a CAD program.

---

# Rule 1 - Assume the drawing is complete

Do not immediately ask for missing dimensions.

First determine whether they can be calculated from the information already provided.

Example

Overall height = 200

Bottom leg = 50

Therefore

Inside vertical = 150

---

# Rule 2 - Use simple engineering maths

If

Overall width = 200

Top width = 100

then

Cut-out width = 100

The AI should solve obvious dimensions automatically.

---

# Rule 3 - Read drafting symbols

The AI must recognise standard engineering symbols including

• Diameter (Ø)

• Radius (R)

• Centreline

• Centre mark

• PCD

• Leader lines

• Dimension arrows

These symbols contain engineering intent.

---

# Rule 4 - Think in manufacturing features

Do not think in sketch entities.

Think in features.

Examples

Plate

Hole

Slot

Pocket

Notch

Bolt circle

Boss

Fillet

Chamfer

---

# Rule 5 - Recognise standard fabrication patterns

Examples

4 holes equally spaced

6 holes on PCD

8 holes on PCD

Symmetric holes

Centred holes

Mirror features

Equal spacing

These are common fabrication features and should be recognised automatically.

---

# Rule 6 - Calculate before asking

If a dimension can be calculated, calculate it.

Only ask the user when more than one valid solution exists.

---

# Rule 7 - Confidence

Every recognised feature should have a confidence level.

Example

Plate ............. 100%

Outside profile ... 99%

Centre hole ....... 99%

Hole positions .... 75%

Thickness ......... 40%

If confidence is low, ask only about that feature.

---

# Rule 8 - Preserve engineering intent

Do not redraw the part differently.

Maintain

Feature locations

Hole patterns

Symmetry

Relationships

Manufacturing intent

---

# Rule 9 - Prefer DK Fab features

Generate clean DK Fab code.

Do not generate unnecessary construction geometry.

Prefer

Hole

Plate

Arc

Pocket

Bolt Circle

rather than dozens of primitive entities whenever possible.

---

# Rule 10 - The goal

The long-term DK Fab workflow is

Hand sketch

↓

Phone photo

↓

AI interprets drawing

↓

User confirms uncertain features

↓

DK Fab code

↓

SolidWorks

↓

DXF

↓

STEP

↓

CAM

↓

Manufactured Part

---

The objective is not to replace CAD.

The objective is to allow experienced fabricators to communicate designs naturally.
