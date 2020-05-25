"""
Given a smaller string s and a bigger string b, design an algorithm
to find all permuta­tions of the shorter string within the longer one. Print the location of each permutation.
"""

import math

# import itertools
# print(list(itertools.permutations([1, 2, 3])))

# def get_permutations(nums):
#     # how to print all permutations of this?
#     for num in nums:
#         print(num)
#     return []

def all_perms(elements):
    if len(elements) <=1:
        print('elements base case', elements)
        yield elements
    else:
        print('elements', elements)
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

if __name__ == '__main__':
    
    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'

    sorted_s = ''.join(sorted(s))
    print('sorted_s', sorted_s)

    list_perms = []
    len_s = len(s)
    for i in range(len(b) - len_s + 1):
        if b[i] not in s:
            continue
        perm = b[i:i+len_s]
        sorted_perm = ''.join(sorted(perm))
        # print('i', i, 'sorted_perm', sorted_perm)
        if sorted_s == sorted_perm:
            list_perms.append(
                (i, perm)
            )
    print(list_perms)


    # combination is when order doesn't matter, like a salad with ingredients in different order
    # permutations is when order matters, like a security look that will only work in the right order

    # permutations with repetitions of n things in groups of r: n ** r

    # permutations without repetitions where n is the number of things to choose r from: n! / (n - r)!
    # if we want all things then r = n and because 0! = 1 the number of permutations is: n!

    # nums = [1, 2, 3]
    # count_nums = len(nums)
    # print('count_nums', count_nums)
    # print('possible permutations', math.factorial(count_nums))

    # print(get_permutations(nums))

    # convert iterator to list
    # permutations = list(all_perms(nums))
    # print(permutations)
    
    # use for loop with iterator
    # for perm in all_perms(nums):
    #     print(perm)




