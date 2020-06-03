# find a, b, c, d (each between 1 and 1000) where a**3 + b**3 = c**3 + d**3

def find_nums_bf(n):
    tuples = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                # for d in range(1, n + 1):
                #     if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                #         tuples.append((a, b, c, d))
                #         # stop on the first d that matches
                #         break
                # just compute d
                d = pow((a ** 3 + b ** 3 - c ** 3), 1/3)
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    tuples.append((a, b, c, int(d)))
    return tuples

def find_nums_2(n):
    tuples = []
    result_pairs = {}
    for c in range(1, n + 1):
        for d in range(1, n + 1):
            result = c ** 3 + d ** 3
            result_pairs[result] = result_pairs.get(result, [])
            result_pairs[result].append((c, d))
    # for a in range(1, n + 1):
    #     for b in range(1, n + 1):
    #         result = a ** 3 + b ** 3
    #         match_list = result_pairs[result]
    #         for pair in match_list:
    #             tuples.append((a, b, pair[0], pair[1]))
    # no need to generate a, b as we already have the pairs in the result_pairs map
    for result, pairs in result_pairs.items():
        # print(result, pairs)
        for pair1 in pairs:
            for pair2 in pairs:
                tuples.append((pair1[0], pair1[1], pair2[0], pair2[1]))

    return tuples

if __name__ == '__main__':
    n = 100
    # print(find_nums_bf(n))
    print(find_nums_2(n))
