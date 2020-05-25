def find_max_square(matrix):
    # print(matrix)
    return None

# const findMaxSquare = (matrix) => {
#     // Time complexity : O(mn). Single pass.
#     // Space complexity : O(mn)

#     // this will shallow copy so it won't be a real clone
#     // const cache = [...matrix];
#     const cache = [];
#     let result = 0;
#     const rows = matrix.length;
#     const cols = matrix[0].length;
    
#     for (i = 0 ; i < rows; i++) {
#         // spread can simplify cloning making a shallow copy of each row
#         cache.push([...matrix[i]]);
#         // this would be copying each value per column
#         // cache.push([]);
#         // for (j = 0; j < cols; j++) {
#         //     cache[i].push(matrix[i][j]);
#         // }
#     }

#     for (i = 0 ; i < rows; i++) {
#         for (j = 0; j < cols; j++) {
#             if (i == 0 || j == 0) {
#                 // do nothing for top row or left column
#                 // cache[i][j] = matrix[i][j];
#             } else if (matrix[i][j] > 0) {
#                 cache[i][j] = 1 + Math.min(...[
#                     cache[i - 1][j],
#                     cache[i][j - 1],
#                     cache[i - 1][j - 1],
#                 ]);
#             }
#             if (cache[i][j] > result) {
#                 result = cache[i][j];
#             }
#         }
#     }
#     // print('cache');
#     // print(cache);
#     return result;

# };

# const maxSquareBruteForce = findMaxSquareBruteForce(matrix);
# print('maxSquareBruteForce', maxSquareBruteForce);

# const maxSquare = findMaxSquare(matrix);
# print('maxSquare', maxSquare);

if __name__ == '__main__':

    matrix = [
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
    ]

    # matrix = [
    #     [1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [1, 0, 0, 1, 0],
    # ]

    # matrix = [
    #     [1, 1],
    #     [1, 1],
    #     [1, 1],
    # ]

    print('matrix')
    for row in matrix:
        print(row)

    print('max_square', find_max_square(matrix))

