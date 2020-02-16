
def prefix_average1(s):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j]
    """
    n = len(s)
    a = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
            a[j] = total / (j+1)
    return a

if __name__ == '__main__':
    print("prefix averages")
    s = [1, 2, 3]
    a = prefix_average1(s)
    print(s)
    print(a)
