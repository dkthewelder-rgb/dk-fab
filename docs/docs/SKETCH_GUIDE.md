# DK Fab Sketch Interpretation Guide

## Purpose

This guide teaches AI systems how to interpret fabrication sketches for DK Fab.

The objective is not to copy a drawing.

The objective is to understand the engineering intent.

---

# Rule 1 - Think like a fabricator

Read the sketch as an experienced fabricator would.

Do not think like a CAD program.

A fabricator automatically calculates simple dimensions and recognises common engineering practice.

---

# Rule 2 - Calculate before asking

Always use simple mathematics before asking the user.

Example

Overall height = 200

Bottom leg = 50

Therefore

Inside vertical = 150

Another example

Overall width = 200

Top width = 100

Therefore

Cut-out width = 100

If a dimension can be calculated, calculate it.

---

# Rule 3 - Read engineering symbols

Recognise standard drafting symbols including:

Diameter (Ø)

Radius (R)

Centreline

Centre mark

PCD

Leader lines

Dimension arrows

Hidden lines

These symbols contain engineering intent.

---

# Rule 4 - Recognise manufacturing features

A drawing is not simply lines.

Recognise features such as:

Plate

Hole

Slot

Pocket

Notch

Bolt circle

Boss

Fillet

Chamfer

Arc

These should become DK Fab geometry.

---

# Rule 5 - Recognise common fabrication patterns

Examples include:

Evenly spaced holes

Bolt circles

Symmetrical features

Centred holes

Mirror geometry

Common motor mounting patterns

Bearing mounting patterns

Wheel spacer patterns

The AI should recognise these whenever possible.

---

# Rule 6 - Use engineering assumptions

If information is missing but only one sensible engineering solution exists, use it.

State the assumption.

Example

"Hole positions assumed centred."

---

# Rule 7 - Ask only when required

Do not ask unnecessary questions.

Only ask when multiple valid interpretations exist.

---

# Rule 8 - Report assumptions

If assumptions are made, list them clearly before the DK Fab code.

---

# Rule 9 - Confidence

Every recognised feature has a confidence.

Example

Plate ............ 100%

Outside profile .. 100%

Centre hole ...... 99%

Hole position .... 70%

Thickness ........ 40%

Low confidence features should be confirmed with the user.

---

# Rule 10 - Preserve design intent

Never redesign the part.

Maintain:

Hole locations

Symmetry

Feature relationships

Manufacturing intent

---

# Rule 11 - Prefer existing examples

Before generating DK Fab code:

Search Model Success examples.

Reuse successful methods whenever possible.

Do not invent new syntax.

---

# Long Term Goal

Hand sketch

↓

Phone photo

↓

AI interprets sketch

↓

User confirms uncertain features

↓

DK Fab code

↓

SolidWorks

↓

DXF / STEP

↓

Manufactured part
