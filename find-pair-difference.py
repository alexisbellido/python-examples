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
    print('------')
    sorted_nums = sorted(nums)
    print(sorted_nums)
    dict_nums = {}
    for num in nums:
        dict_nums[num] = True
    print(dict_nums)
    pairs = []
    return pairs

if __name__ == '__main__':
    nums = [1, 7, 5, 9, 2, 12, 3]
    k = 2

    pairs = find_pairs_bf(nums, k)
    print(pairs)

    pairs = find_pairs_2(nums, k)
    print(pairs)
