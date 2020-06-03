def rotate_matrix(matrix):

    n = len(matrix)
    print('n', n)

    for i in range(n):
        print(matrix[i])

    print('matrix')
    for row in matrix:
        print(row)

if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ]

    rotate_matrix(matrix)