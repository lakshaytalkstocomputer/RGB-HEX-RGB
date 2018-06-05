import rgbToHex
import hexToRgb


def convert():

    welcome_text = """\n\nWelcome to RGB-HEX-RGB converter
Enter 1 to convert RGB to HEX
Enter 2 to convert HEX to RGB
Enter Q to Exit : """

    while True:
        choice = input(welcome_text)
        if choice == "1":
            rgbToHex.to_hex()
        elif choice == "2":
            hexToRgb.to_rgb()
        else:
            break


convert()
