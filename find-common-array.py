def out_of_bounds(a, b, c, x, y, z):
    return x >= len(a) or y >= len(b) or z >= len(c)

def find_common(a, b, c):
    # loop three arrays at the same time
    # these are the indexes
    x = 0
    y = 0
    z = 0
    result = []

    while not out_of_bounds(a, b, c, x, y, z):
        if a[x] == b[y] and b[y] == c[z]:
            result.append(a[x])
            x += 1
            y += 1
            z += 1
        elif a[x] < b[y]:
            x += 1
        elif b[y] < c[z]:
            y += 1
        else:
            z += 1
    return result

if __name__ == '__main__':
    a = [2, 6, 9, 11, 13, 17]
    b = [3, 6, 7, 10, 13, 18]
    c = [4, 5, 6, 9, 11, 13]

    # a = [2, 6, 6, 9, 10]
    # b = [1, 6, 6, 10]
    # c = [4, 6, 6, 7, 10]

    print(find_common(a, b, c))