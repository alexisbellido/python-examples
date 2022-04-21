def unique1(S):
    """
    Return True if there are no duplicate elements in sequence S.

    Quadratic time.
    """
    
    # print('len(S)', len(S))
    # print('====')
    
    # inner loop runs n - 1, n - 2 ... 2, 1 times, which turns into n(n-1) / 2, from the summation of 1 to n resulting in n(n + 1) / 2
    for j in range(len(S)):
        # print(f"j: {j}")
        for k in range(j+1, len(S)):
            # print(f"k: {k}")
            # print(f"S[j]: {S[j]} - S[k]: {S[k]}")
            if S[j] == S[k]:
                return False
        # print('====')
    
    return True

def unique2(S):
    """
    Return True if there are no duplicate elements in sequence S.

    n log(n) time.
    """

    # sorted runs in n log(n)
    temp = sorted(S)

    # loop runs n times so it's O(n)
    for j in range(1, len(temp)):
        print(f"j: {j} - S[j-1]: {S[j-1]} - S[j]: {S[j]}")
        if S[j-1] == S[j]:
            return False
    
    # so the function runs in n log(n)

    return True

if __name__ == '__main__':
    
    s1 = [1, 2, 3, 4]

    print('unique1', unique1(s1))
    print('--')

    print('unique2', unique2(s1))
    print('--')