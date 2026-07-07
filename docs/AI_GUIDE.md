# DK Fab AI Guide

## Core idea

DK Fab is not trying to be a smart CAD system.

DK Fab is a simple executor.

The AI is responsible for understanding the job, choosing dimensions, applying engineering logic, and writing valid DK Fab code.

---

## Main rule

Do not invent DK Fab syntax.

Use the language exactly as documented and copy patterns from working examples.

---

## How the AI should think

Think like a fabricator, welder, machinist, fitter, or maintenance engineer.

The user may describe a part in normal workshop language.

Example:

"Make me a 12mm plate with 8 holes on a 100 PCD."

The AI should understand this as a manufacturing request and convert it into DK Fab geometry.

---

## Before writing code

The AI should:

1. Understand the part.
2. Identify all manufacturing features.
3. Search existing examples if available.
4. Use simple maths to infer dimensions.
5. Ask questions only if needed.
6. State assumptions.
7. Output valid DK Fab code.

---

## Engineering maths

Do simple calculations before asking questions.

Example:

Overall height = 200

Bottom leg = 50

Therefore inside vertical = 150

Do not ask for dimensions that are already implied.

---

## Common features

The AI should recognise common fabrication features:

- plate
- hole
- slot
- notch
- cut-out
- PCD
- bolt circle
- centre bore
- clearance hole
- lightening hole
- chamfer
- radius
- rounded corner

---

## Example status levels

Use these folders or labels:

### Generated

Code was generated but not tested.

### Model Success

Code parsed and created the expected SolidWorks model.

### Field Verified

The part was manufactured and physically tested.

---

## Safety

DK Fab code can create real parts.

For safety-critical parts, always warn users to verify dimensions, material, fitment, strength, and legality.

Safety-critical examples include:

- wheel spacers
- suspension parts
- steering parts
- lifting parts
- pressure parts
- brake parts
- structural vehicle parts

---

## Long term direction

The goal is:

Natural language

↓

AI

↓

DK Fab

↓

SolidWorks

↓

DXF / STEP / CAM

↓

Manufactured part

Future versions may include hand sketch interpretation, phone photo input, LiDAR assistance, turned parts, sheet metal, CNC machining, and a community part dimension library.
