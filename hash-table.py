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
    for k in d:
        print(k, d[k])

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



