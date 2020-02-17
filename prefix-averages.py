
def prefix_average1(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    O(n^2)
    """
    n = len(s)
    a = [0] * n # create list of n zeros
    for j in range(n):
        total = 0
        for i in range(j + 1):
            print(f"j is {j} - i is {i} - s[i] is {s[i]}")
            total += s[i]
            a[j] = total / (j+1)
        print('===')
    return a


def prefix_average2(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    O(n^2)
    """
    n = len(s)
    a = [0] * n # create list of n zeros
    for j in range(n):
        a[j] = sum(s[0:j+1]) / (j+1)
    return a


def prefix_average3(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    O(n)
    """
    n = len(s)
    a = [0] * n # create list of n zeros
    total = 0
    for j in range(n):
        total += s[j]
        a[j] = total / (j+1)
    return a

if __name__ == '__main__':
    print("prefix averages")
    s = [1, 2, 3]
    print(s)
    print(prefix_average1(s))
    print(prefix_average2(s))
    print(prefix_average3(s))
