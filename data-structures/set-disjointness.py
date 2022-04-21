def disjoint1(A, B, C):
    """
    Return True if there's no element common to all three lists
    This version runs in cubic time.
    """
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

if __name__ == '__main__':
    
    A = [1, 2, 3]
    B = [4, 5, 3]
    C = [7, 8, 3]

    print(disjoint1(A, B, C))