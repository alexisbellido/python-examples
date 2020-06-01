import copy

def find_max_square(matrix):
    """
    Time complexity : O(mn). Single pass.
    Space complexity : O(mn)
    """
    cache = copy.deepcopy(matrix)
    result = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                # do nothing for top-most row or left-most column as cache is a clone of matrix
                # cache[i][j] = matrix[i][j]
                continue
            else:
                if matrix[i][j] > 0:
                    cache[i][j] = 1 + min(
                        cache[i][j-1],
                        cache[i-1][j],
                        cache[i-1][j-1]
                    )
            if cache[i][j] > result:
                result = cache[i][j]
    return result

if __name__ == '__main__':

    matrix_1 = [
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
    ]

    matrix_2 = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    ]

    matrix_3 = [
        [1, 1],
        [1, 1],
        [1, 1],
    ]

    print('matrix_1')
    # for row in matrix_1:
    #     print(row)

    print('find_max_square(matrix_1)', find_max_square(matrix_1))
    print('find_max_square(matrix_2)', find_max_square(matrix_2))
    print('find_max_square(matrix_3)', find_max_square(matrix_3))

