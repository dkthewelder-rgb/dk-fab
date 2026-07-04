import win32com.client
import time
import math
from compiler import polygon_to_lines

TEMPLATE_PATH = r"C:\ProgramData\SolidWorks\SOLIDWORKS 2026\templates\Part.prtdot"
SAVE_FOLDER = r"C:\Users\GGPC\Documents\AI SolidWorks Designer"


def parse_values(parts):
    values = {}
    for item in parts:
        key, value = item.split("=")
        try:
            values[key.lower()] = float(value)
        except ValueError:
            values[key.lower()] = value
    return values


def read_dkfab(filename):
    part_name = "dkfab_part"
    plate = None
    outer_profile = []
    entities = []
    save_name = None
    mode = None

    with open(filename, "r") as f:
        for raw in f.readlines():
            line = raw.strip()
            if line == "" or line.startswith("#"):
                continue

            parts = line.split()
            command = parts[0].upper()

            if command in ("PROFILE", "END_PROFILE", "SKETCH", "END_SKETCH"):
                values = {}
            else:
                values = parse_values(parts[1:])

            if command == "PART":
                part_name = values["name"]

            elif command == "PLATE":
                plate = {
                    "width": values["width"],
                    "height": values["height"],
                    "thickness": values["thickness"]
                }

            elif command == "PROFILE":
                if len(parts) > 1 and parts[1].lower() == "outer":
                    mode = "outer_profile"

            elif command == "END_PROFILE":
                mode = None

            elif command == "SKETCH":
                mode = "cut_sketch"

            elif command == "END_SKETCH":
                mode = None

            elif command == "POLYGON":
                line_commands = polygon_to_lines(
                    values["x"],
                    values["y"],
                    values["sides"],
                    values["diameter"],
                    values.get("angle", 0)
                )

                for line_cmd in line_commands:
                    line_parts = line_cmd.split()
                    line_values = parse_values(line_parts[1:])

                    if mode == "outer_profile":
                        outer_profile.append(("line", line_values))
                    elif mode == "cut_sketch":
                        entities.append(("line", line_values))

            elif command == "LINE":
                if mode == "outer_profile":
                    outer_profile.append(("line", values))
                elif mode == "cut_sketch":
                    entities.append(("line", values))

            elif command == "CIRCLE":
                if mode == "cut_sketch":
                    entities.append(("circle", values))

            elif command == "ARC":
                if mode == "outer_profile":
                    outer_profile.append(("arc", values))
                elif mode == "cut_sketch":
                    entities.append(("arc", values))

            elif command == "SLOT":
                if mode == "cut_sketch":
                    entities.append(("slot", values))

            elif command == "SAVE":
                save_name = values["name"]

    if plate is None:
        raise Exception("No PLATE command found.")

    if save_name is None:
        save_name = part_name

    return plate, outer_profile, entities, save_name


def draw_line(part, values):
    part.SketchManager.CreateLine(
        values["x1"] / 1000,
        values["y1"] / 1000,
        0,
        values["x2"] / 1000,
        values["y2"] / 1000,
        0
    )


def draw_circle(part, values):
    x = values["x"] / 1000
    y = values["y"] / 1000
    r = values["diameter"] / 2000

    part.SketchManager.CreateCircle(
        x, y, 0,
        x + r, y, 0
    )


def draw_arc(part, values):
    cx = values["x"] / 1000
    cy = values["y"] / 1000
    r = values["radius"] / 1000

    start_angle = math.radians(values["start"])
    end_angle = math.radians(values["end"])

    sx = cx + math.cos(start_angle) * r
    sy = cy + math.sin(start_angle) * r

    ex = cx + math.cos(end_angle) * r
    ey = cy + math.sin(end_angle) * r

    part.SketchManager.CreateArc(
        cx, cy, 0,
        sx, sy, 0,
        ex, ey, 0,
        1
    )


def draw_slot(part, values):
    x = values["x"] / 1000
    y = values["y"] / 1000
    length = values["length"] / 1000
    width = values["width"] / 1000
    angle = math.radians(values.get("angle", 0))

    center_distance = length - width

    dx = math.cos(angle)
    dy = math.sin(angle)

    x1 = x - dx * center_distance / 2
    y1 = y - dy * center_distance / 2

    x2 = x + dx * center_distance / 2
    y2 = y + dy * center_distance / 2

    # SolidWorks native slot:
    # 0 = center line slot
    # 0 = center-to-center length
    part.SketchManager.CreateSketchSlot(
        0,
        0,
        width,
        x1, y1, 0,
        x2, y2, 0,
        0, 0, 0,
        1,
        False
    )


def draw_entity(part, entity_type, values):
    if entity_type == "line":
        draw_line(part, values)
    elif entity_type == "circle":
        draw_circle(part, values)
    elif entity_type == "arc":
        draw_arc(part, values)
    elif entity_type == "slot":
        draw_slot(part, values)


def build_part(plate, outer_profile, entities, save_name):
    sw = win32com.client.GetActiveObject("SldWorks.Application")
    sw.Visible = True

    sw.NewDocument(TEMPLATE_PATH, 0, 0, 0)
    time.sleep(1)

    part = sw.ActiveDoc

    front_plane = part.FeatureByName("Front Plane")
    front_plane.Select2(False, 0)

    part.SketchManager.InsertSketch(True)

    if len(outer_profile) > 0:
        for entity_type, values in outer_profile:
            draw_entity(part, entity_type, values)
    else:
        part.SketchManager.CreateCenterRectangle(
            0, 0, 0,
            plate["width"] / 2000,
            plate["height"] / 2000,
            0
        )

    for entity_type, values in entities:
        draw_entity(part, entity_type, values)

    part.ShowNamedView2("*Trimetric", 8)
    part.ViewZoomtofit2()

    part.FeatureManager.FeatureExtrusion2(
        True, False, False,
        0, 0,
        plate["thickness"] / 1000,
        plate["thickness"] / 1000,
        False, False, False, False,
        0.0174532925199433,
        0.0174532925199433,
        False, False, False, False,
        True, True, True,
        0, 0, False
    )

    part.SketchManager.InsertSketch(True)

    filepath = rf"{SAVE_FOLDER}\{save_name}.SLDPRT"
    part.SaveAs3(filepath, 0, 0)

    print("Saved:", filepath)
    print("DK Fab compiler build finished.")


plate, outer_profile, entities, save_name = read_dkfab("dkfab.txt")
build_part(plate, outer_profile, entities, save_name)