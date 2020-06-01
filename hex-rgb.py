def hexToRgb(value):
    # Convert string to hexadecimal number (base 16)
    num = (int(value.lstrip("#"), 16))

    # Shift 16 bits to the right, and then binary AND to obtain 8 bits representing red
    r = ((num >> 16) & 0xFF)

    # Shift 8 bits to the right, and then binary AND to obtain 8 bits representing green
    g = ((num >> 8) & 0xFF)

    # Simply binary AND to obtain 8 bits representing blue
    b = (num & 0xFF)
    return (r, g, b)

if __name__ == "__main__":
    print(hexToRgb("#f5e942")) # RGB: 245, 233, 66
    print(0b111)

    print(int('0x10', 16))
    print(int(0x10))

    print(int(0b1111))
    print(int('0b1011', 2))
    