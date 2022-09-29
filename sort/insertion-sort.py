def insertion_sort(A):
    for k in range(1, len(A)):
        """outer loop starts after the first element, which is assumed to be sorted against itself"""
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            """inner loop compares elements int the array before the current value and sort them"""
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
    return A

if __name__ == '__main__':
    nums = [8, 2, 3 ,4, 1]
    print('original', nums)
    print('sorted', insertion_sort(nums))
