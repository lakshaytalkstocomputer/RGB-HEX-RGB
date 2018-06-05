def to_rgb():
    entry_text = """\nEnter HEX value of colour. Please enter only hex value.
Eg- if the hex value of your colour is 0x0688ff then enter only 0688ff : """
    hex_code = input(entry_text)

    try :
        deci_val = int(hex_code, 16)

    except ValueError:
        print("Invalid Hxadecimal Code. ")
        return

    blue_value = deci_val % 256
    deci_val =  deci_val >> 8
    green_value = deci_val % 256
    deci_val = deci_val >> 8
    red_value = deci_val % 256


    print("RGB  : ({0},{1},{2})".format(red_value, green_value, blue_value))
