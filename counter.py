from collections import Counter

if __name__ == "__main__":
    c1 = Counter('gallahad')
    print(c1)
    print('c1.most_common(2)', c1.most_common(2))

    print('keys in c1')
    for k in c1:
        print(k)

    print('keys and values in c1.items()')
    for k,v in c1.items():
        print(k, v)

    c2 = Counter({'red': 4, 'blue': 2})
    print(c2)

    c3 = Counter(cats=4, dogs=8)
    print(c3)

    c4 = Counter(['egg', 'ham', 'cheese', 'cheese'])
    print(c4)
    print('olive', c4['olive'])
    print('cheese', c4['cheese'])