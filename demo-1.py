import re

# Write a function that takes a hex color code such as #FFFFFF or #00ff00 and classifies whether it
# is a grayscale color or not.

def hexToDecimal(code):
    m = re.search(r'#(.{2})(.{2})(.{2})', code)
    r = m.group(1)
    g = m.group(2)
    b = m.group(3)
    return {
        'r': int(r, 16),
        'g': int(g, 16),
        'b': int(b, 16),
    }

def isGrayish(components, delta=0):
    max_delta = 0
    rg = abs(components['r'] - components['g'])
    gb = abs(components['g'] - components['b'])
    br = abs(components['b'] - components['r'])
    l = [rg, gb, br]
    for d in l:
        if d > max_delta:
            max_delta = d
    return ( max_delta <= delta )
    

if __name__ == '__main__':
    # color = '#808080'
    # color = '#008000'
    # color = '#ff0000'
    color = '#b5b4b3'
    components = hexToDecimal(color)
    print(components)
    isGrayish = isGrayish(components, 2)
    print(f'{color} is a kind of gray: {isGrayish}')
    