from time import process_time

def set_end_position(i, j, input, output, index):
    num_rows = len(input)
    num_cols = len(input[0])
    skip_number = 5

    # flag to check column
    col_edge = 0

    # flag to check row edge
    row_edge = 0

    print('---------------------------------')
    print('i', i, 'j', j)
    for m in range(i, num_rows):
        # loop breaks where first 1 encounters
        print('m', m, 'j', j)
        if input[m][j] == 1:
            row_edge = 1
            break

        # pass because already processed
        if input[m][j] == skip_number:
            pass

        for n in range(j, num_cols):
            # loop breaks where first 1 encounters
            if input[m][n] == 1:
                col_edge = 1
                break

            # fill rectangle elements with any number so that we can exclude next time
            input[m][n] = skip_number

    if row_edge == 1:
        output[index].append(m - 1)
    else:
        # when end point touch the boundary
        output[index].append(m)

    if col_edge == 1:
        output[index].append(n - 1)
    else:
        # when end point touch the boundary
        output[index].append(n)
    print('---------------------------------')


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

    output = []

    # used to store start and end position in same index
    index = -1

    num_rows = len(input)
    print('num_rows', num_rows)

    num_cols = len(input[0])
    print('num_cols', num_cols)

    for i in range(0, num_rows):
        # print(f'Row: {i:*>2} | ', end=' ')
        # print(f'Row: {i:>2} | ', end=' ')
        for j in range(0, num_cols):
            # print(input[i][j], end=' ')
            if input[i][j] == 0:
                output.append([i, j])
                # use to store last position
                index = index + 1
                set_end_position(i, j, input, output, index)
        # print()

    print(output)

    # start_time = process_time()
    # for x in range(10000):
    #     pass
    # end_time = process_time()
    # elapsed = end_time - start_time
    # print(f"elapsed {elapsed}")
