if __name__ == '__main__':
    nums = [1, 3, 5, 7]
    animals = ['cat', 'dog', 'horse', 'eagle']
    len_nums = len(nums)
    len_animals = len(animals)

    for animal in animals:
        hash_code = hash(animal)
        index = hash_code % len_animals
        print(animal, hash_code, index)

    # a try sorting dict by key
    d = {
        2: 'monkey',
        1: 'snake',
        5: 'cow',
    }
    # unsorted
    # for k in d:
    #     print(k, d[k])
    # print items in dictionary as tuples
    # print(d.items())
    # sort those tuples
    # print(sorted(d.items()))
    # loop over them and print elements from original dictionary in sorted order
    for item in sorted(d.items()):
        print(item[0], d[item[0]])

    # find pairs of elements from a and b that add up closest to sum
    # brute force
    print('=== using brute force')
    a = [-1, 3, 8, 2, 9, 5]
    b = [4, 1, 2, 10, 5, 20]
    sum = 24
    a_b_map = {}
    for i in a:
        for j in b:
            a_b_map.setdefault(i + j, []).append((i, j))
    delta = 0
    found = 0
    while found < 2:
        if (sum + delta) in a_b_map:
            print(sum + delta, a_b_map[sum + delta])
            found += 1
        if (sum - delta) in a_b_map:
            print(sum - delta, a_b_map[sum - delta])
            found += 1
        delta += 1

    # using a set to put all elements of a and then loop over b checking if
    # set_a contains a number that produces the sum or something close with a delta
    print('=== using set')
    set_a = set(a)
    sum = 24
    delta = 0
    found = 0
    while found < 2:
        for j in b:
            if (sum - j) + delta in set_a:
                # print('add to found X')
                print(sum + delta, (sum - j) + delta, j)
                found += 1
            if (sum - j) - delta in set_a:
                # print('add to found Y')
                print(sum - delta, (sum - j) - delta, j)
                found += 1
        delta += 1

