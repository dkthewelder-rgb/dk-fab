import math


def polygon_to_lines(x, y, sides, diameter, angle=0):
    radius = diameter / 2
    start = math.radians(angle)

    points = []

    for i in range(int(sides)):
        a = start + (2 * math.pi * i / int(sides))
        px = x + math.cos(a) * radius
        py = y + math.sin(a) * radius
        points.append((px, py))

    lines = []

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        lines.append(
            f"LINE x1={x1:.3f} y1={y1:.3f} x2={x2:.3f} y2={y2:.3f}"
        )

    return lines


def slot_to_entities(x, y, length, width, angle=0):
    if length <= width:
        raise Exception("SLOT length must be bigger than width")

    a = math.radians(angle)
    r = width / 2
    half_center = (length - width) / 2

    dx = math.cos(a)
    dy = math.sin(a)

    px = -math.sin(a)
    py = math.cos(a)

    c1x = x - dx * half_center
    c1y = y - dy * half_center
    c2x = x + dx * half_center
    c2y = y + dy * half_center

    p1x = c1x + px * r
    p1y = c1y + py * r
    p2x = c2x + px * r
    p2y = c2y + py * r

    p3x = c2x - px * r
    p3y = c2y - py * r
    p4x = c1x - px * r
    p4y = c1y - py * r

    return [
        ("line", {
            "x1": p1x,
            "y1": p1y,
            "x2": p2x,
            "y2": p2y
        }),

        ("arc", {
            "x": c2x,
            "y": c2y,
            "radius": r,
            "start": angle + 90,
            "end": angle - 90,
            "direction": 1
        }),

        ("line", {
            "x1": p3x,
            "y1": p3y,
            "x2": p4x,
            "y2": p4y
        }),

        ("arc", {
            "x": c1x,
            "y": c1y,
            "radius": r,
            "start": angle - 90,
            "end": angle + 90,
            "direction": 1
        }),
    ]