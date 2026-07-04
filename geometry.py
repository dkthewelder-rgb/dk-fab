import math


def polygon_points(x, y, sides, diameter, angle=0):
    points = []
    radius = diameter / 2
    start_angle = math.radians(angle)

    for i in range(sides):
        a = start_angle + (2 * math.pi * i / sides)
        px = x + math.cos(a) * radius
        py = y + math.sin(a) * radius
        points.append((px, py))

    return points


def rectangle_points(x, y, width, height, angle=0):
    hw = width / 2
    hh = height / 2

    points = [
        (-hw, -hh),
        ( hw, -hh),
        ( hw,  hh),
        (-hw,  hh),
    ]

    return rotate_points(points, x, y, angle)


def triangle_points(x, y, width, height, angle=0):
    points = [
        (0, height / 2),
        (width / 2, -height / 2),
        (-width / 2, -height / 2),
    ]

    return rotate_points(points, x, y, angle)


def rotate_points(points, x, y, angle):
    rotated = []
    a = math.radians(angle)

    for px, py in points:
        rx = x + px * math.cos(a) - py * math.sin(a)
        ry = y + px * math.sin(a) + py * math.cos(a)
        rotated.append((rx, ry))

    return rotated


def lines_from_points(points, closed=True):
    lines = []

    for i in range(len(points) - 1):
        lines.append((points[i], points[i + 1]))

    if closed and len(points) > 2:
        lines.append((points[-1], points[0]))

    return lines