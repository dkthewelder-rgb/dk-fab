# AI START HERE

This repository is for DK Fab.

DK Fab is a simple fabrication geometry language.

DK Fab should stay dumb and exact.

The AI does the thinking.

---

## Before generating DK Fab code

An AI must read and follow the project documentation.

Do not guess the syntax.

Do not invent commands.

Use existing working examples whenever possible.

---

## Required AI behaviour

Before writing DK Fab code, the AI should:

1. Read the DK Fab language rules.
2. Look at working examples.
3. Use simple engineering maths.
4. Think like a fabricator.
5. Ask questions only when required.
6. Clearly state assumptions.
7. Generate clean DK Fab code.
8. Prefer code that already matches proven examples.

---

## Important principle

The user should be able to say things like:

"Make me a GX200 engine mount plate"

or

"Make me a 10mm wheel spacer for a 1990 Toyota Hilux 2WD"

The AI should find or infer the useful dimensions, then output simple DK Fab geometry.

DK Fab itself does not need to know what a GX200 or Hilux is.

The AI knows that.

DK Fab only builds the geometry.

---

## Status levels for examples

Use these levels:

### Generated

AI created the DK Fab code, but it has not been tested.

### Model Success

The DK Fab code parsed correctly and built a SolidWorks model successfully.

### Field Verified

The part was manufactured and physically tested.

Only field verified parts should be trusted for real-world use.

---

## Safety

Fabricated parts can be dangerous if wrong.

Wheel spacers, vehicle parts, lifting parts, suspension parts, steering parts, pressure parts and structural parts must be checked carefully before manufacture or use.

AI generated DK Fab code is a starting point, not automatic proof of safety.

---

## Long term goal

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

DXF / STEP / CAM

↓

Manufactured part
