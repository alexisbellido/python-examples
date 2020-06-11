def get_longest(input):
    prev = None
    max_count = 0
    for cur in input:
        if cur != prev:
            running_count = 1
        else:
            running_count += 1
        if running_count > max_count:
            max_count = running_count
            result = {cur: max_count}
        prev = cur
    print(result)


if __name__ == '__main__':
    input = 'AABCDDBBBEA'
    # input = 'AABCDDBBBEAAAA'
    # input = 'AAAAAA'
    get_longest(input)