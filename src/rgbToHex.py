
def to_hex():
    red = int(input("\nEnter value of RED : "))
    if not 0 <= red <= 255:
        print("Invalid Value.")
        return

    green = int(input("Enter value of GREEN : "))
    if not 0 <= green <= 255:
        print("Invalid Value.")
        return

    blue = int(input("Enter value of BLUE : "))
    if not 0 <= blue <= 255:
        print("Invalid Value.")
        return

    hex_value = (red << 16) + (green << 8) + blue

    print("Hex Value for RGB is : " + hex(hex_value))



