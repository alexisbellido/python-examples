# given array of integers find pairs with difference k
# nums = [1, 7, 5, 9, 2, 12, 3] and k = 2, result = [(1,3), (3,5), (5, 7), (7, 9)]

def find_pairs_bf(nums, k):
    """
    brute-force approach that loops over list calculating difference
    """
    pairs = []
    for first in nums:
        for second in nums:
            if abs(first - second) == k:
                if first < second:
                    pair = (first, second)
                else:
                    pair = (second, first)
                if pair not in pairs:
                    pairs.append(pair)
    return pairs

def find_pairs_2(nums, k):
    """
    a better approach
    """
    pairs = []
    sorted_nums = sorted(nums)
    print('k', k, 'sorted', sorted_nums)
    dict_nums = {k: v for k, v in zip(sorted_nums, sorted_nums)}
    for key in dict_nums:
        if (key + k) in dict_nums:
            pair = (key, key + k)
            pairs.append(pair)
    return pairs

if __name__ == '__main__':
    nums = [1, 7, 5, 9, 2, 12, 3]
    k = 2

    print('brute force')
    pairs = find_pairs_bf(nums, k)
    print(pairs)

    print('with hash table 1')
    pairs = find_pairs_2(nums, k)
    print(pairs)

    print('with hash table 2')
    nums = [1, 7, 5, 9, 2, 12, 3]
    k = 3
    pairs = find_pairs_2(nums, k)
    print(pairs)


