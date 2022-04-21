from time import process_time

def prefix_average1(S):
    """
    This runs in quadratic time because of the inner loop.
    """
    n = len(S)
    A = [0] * n

    for j in range(n):
        total = 0
        # print('index j:', j, '- element from S:', S[j])
        for i in range(j + 1):
            # print('i: ', i, 'element', S[i])
            total += S[i]
        A[j] = total / (j + 1)

    return A

def prefix_average3(S):
    """
    This runs in linear time.
    """
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    
    return A

if __name__ == '__main__':

    # seq = [1, 2, 3, 4]
    seq = list(range(10000))
    # print('seq', seq)
    print('---')

    start_time = process_time()
    pa1 = prefix_average1(seq)
    print('pa1')
    # print(pa1)

    end_time = process_time()
    elapsed = end_time - start_time
    print(f"{elapsed}")

    print('---')

    start_time = process_time()
    pa3 = prefix_average3(seq)
    print('pa3')
    # print(pa3)

    end_time = process_time()
    elapsed = end_time - start_time
    print(f"{elapsed}")

    print('---')