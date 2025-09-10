
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def print_roof(height):
    print(" " * int(height) + "_" * (4 * height - 2))  # Roof top line
    for _ in range(1, int(height)):
        # Adjust spaces for each row of the roof
        print(" " * (int(height) - _) + "/" + " " * int(2 * height - 2) + "/" + " " * (2 * (_ - 1)) + "\\" + " " * int(2 * height - 2) + "\\")
    print("T" * (3 * 2 * height - 2))  # Roof base line

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

def print_house(wall_height, roof_height):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    print_roof(roof_height)  # Print the roof

    offset = int((3 * 2 * roof_height - 3 * wall_height) / 2 - 1)
    for _ in range(wall_height - 1):
        # Print each row of the walls, adjusted for offset
        print(" " * offset + "|" + " " * (3 * wall_height - 2) + "|")

    # Print the base row for the walls
    print(" " * offset + "#" * (3 * wall_height))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
wall_height = int(input("Enter wall height: "))
roof_height = int(input("Enter roof height: "))
print_house(wall_height, roof_height)