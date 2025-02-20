from solid import *
from solid.utils import *

# Define enclosure dimensions
WIDTH = 118  # mm (matches Stream Deck faceplate width)
HEIGHT = 84  # mm (matches Stream Deck faceplate height)
DEPTH = 40  # mm (increased to fit Raspberry Pi & battery)
WALL_THICKNESS = 4  # mm

# Internal dimensions after accounting for walls
INNER_WIDTH = WIDTH - 2 * WALL_THICKNESS
INNER_HEIGHT = HEIGHT - 2 * WALL_THICKNESS
INNER_DEPTH = DEPTH - 2 * WALL_THICKNESS

# Cutout dimensions
USB_C_WIDTH = 14  # mm
USB_C_HEIGHT = 8  # mm
RESET_HOLE_DIAMETER = 3  # mm

# Positions
USB_C_POSITION = [WIDTH // 2 - USB_C_WIDTH // 2, WALL_THICKNESS]
RESET_HOLE_POSITION = [WIDTH // 2, HEIGHT - WALL_THICKNESS]

# Function to create the enclosure box
def create_enclosure():
    outer_box = cube([WIDTH, HEIGHT, DEPTH])
    inner_box = translate([WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS])(
        cube([INNER_WIDTH, INNER_HEIGHT, INNER_DEPTH])
    )
    return outer_box - inner_box

# Function to add a cutout (e.g., USB-C or Reset Button)
def add_cutout(obj, width, height, position):
    cutout = cube([width, height, WALL_THICKNESS])
    return obj - translate([position[0], position[1], 0])(cutout)

# Generate enclosure
enclosure = create_enclosure()

# Apply cutouts for USB-C and reset button
enclosure = add_cutout(enclosure, USB_C_WIDTH, USB_C_HEIGHT, USB_C_POSITION)
enclosure = add_cutout(enclosure, RESET_HOLE_DIAMETER, RESET_HOLE_DIAMETER, RESET_HOLE_POSITION)

# Export to OpenSCAD file
scad_file_path = "custom_stream_deck_enclosure.scad"
with open(scad_file_path, "w") as f:
    f.write(scad_render(enclosure))

print(f"SCAD file saved: {scad_file_path}")
