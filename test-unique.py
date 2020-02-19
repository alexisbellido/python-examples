def unique1(S):
    # this function runs in O(n^2)
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            print(f"j: {j} - k: {k}")
            if S[j] == S[k]:
                return False
    return True

def unique2(S):
    # this function runs in O(n log n)
    temp = sorted(S) # this is O(n log n)
    print(temp)
    for j in range(1, len(temp)): # and loop runs n times so it's O(n)
        print(f"j: {j} - (j-1): {j-1}")
        print(f"temp[j-1]: {temp[j-1]} - temp[j]: {temp[j]}")
        if temp[j-1] == temp[j]:
            return False
    return True


if __name__ == '__main__':
    nums = [5, 2, 3, 4, 1, 4]
    print(unique1(nums))
    print(unique2(nums))
