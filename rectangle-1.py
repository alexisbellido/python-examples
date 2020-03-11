from time import process_time

def lookup_set(x, numbers):
    numbers_set = set(numbers)
    if x in numbers_set:
        return True
    return False

if __name__ == '__main__':
    # n = int(input("Enter a number to search for\n"))
    """
    https://www.geeksforgeeks.org/find-rectangles-filled-0/
    We have one 2D array, filled with zeros and ones. We have to find the
    starting point and ending point of all rectangles filled with 0.
    It is given that rectangles are separated and do not touch each other (vertically or horizontally; looks like diagonally is okay)
    however they can touch the boundary of the array.A rectangle might contain
    only one element.
    """

    # input = [
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 0, 0, 0, 1],
    #     [1, 0, 1, 0, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 1, 1],
    #     [1, 0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0, 1],
    #     [1, 1, 1, 1, 1, 1, 1]
    # ]

    input = [
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 0],
    ]

    # input = [
    #     [1, 1, 0, 1, 0],
    # ]

    num_rows = len(input)
    print('num_rows', num_rows)

    # row_index = 0
    # for row in input:
    #     # print(f'Row: {count:*>2} | ', end=' ')
    #     print(f'Row: {row_index:>2} | ', end=' ')
    #     row_index += 1
    #     for col in row:
    #         print(col, end=' ')
    #     print()

    # start_time = process_time()
    # for x in range(10000):
    #     pass
    # end_time = process_time()
    # elapsed = end_time - start_time
    # print(f"elapsed {elapsed}")
