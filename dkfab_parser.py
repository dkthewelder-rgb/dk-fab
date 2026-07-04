from solidworks_api import make_plate, build_cut_sketch


def parse_named_values(parts):
    values = {}

    for item in parts:
        key, value = item.split("=")

        try:
            values[key.lower()] = float(value)
        except ValueError:
            values[key.lower()] = value

    return values


def run_file(filename):
    part_name = None
    plate = None
    save_name = None

    sketches = []
    current_sketch = None

    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        if line == "" or line.startswith("#"):
            continue

        parts = line.split()
        command = parts[0].upper()
        values = parse_named_values(parts[1:])

        if command == "PART":
            part_name = values["name"]

        elif command == "PLATE":
            plate = {
                "width": values["width"],
                "height": values["height"],
                "thickness": values["thickness"]
            }

        elif command == "SKETCH":
            current_sketch = {
                "operation": values["operation"],
                "entities": []
            }

        elif command == "LINE":
            current_sketch["entities"].append({
                "type": "line",
                "x1": values["x1"],
                "y1": values["y1"],
                "x2": values["x2"],
                "y2": values["y2"]
            })

        elif command == "CIRCLE":
            current_sketch["entities"].append({
                "type": "circle",
                "x": values["x"],
                "y": values["y"],
                "diameter": values["diameter"]
            })

        elif command == "ARC":
            current_sketch["entities"].append({
                "type": "arc",
                "x1": values["x1"],
                "y1": values["y1"],
                "x2": values["x2"],
                "y2": values["y2"],
                "cx": values["cx"],
                "cy": values["cy"],
                "direction": values.get("direction", "ccw")
            })

        elif command == "END_SKETCH":
            sketches.append(current_sketch)
            current_sketch = None

        elif command == "SAVE":
            save_name = values["name"]

    if plate is None:
        raise Exception("No PLATE command found.")

    if save_name is None:
        save_name = part_name or "dkfab_part"

    part = make_plate(
        plate["width"],
        plate["height"],
        plate["thickness"]
    )

    for sketch in sketches:
        if sketch["operation"] == "cut":
            build_cut_sketch(part, sketch["entities"])
        else:
            raise Exception("Only SKETCH operation=cut is supported right now.")

    filepath = rf"C:\Users\GGPC\Documents\Solidworks first\AI design test\{save_name}.SLDPRT"
    part.SaveAs3(filepath, 0, 0)

    print("Saved:", filepath)
    print("Primitive DFL build finished.")