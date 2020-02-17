def unique1(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            print(f"j: {j} - k: {k}")
            if S[j] == S[k]:
                return False
    return True

def unique2(S):
    temp = sorted(S)
    print(temp)
    for j in range(1, len(temp)):
        print(f"j: {j} - (j-1): {j-1}")
        print(f"temp[j-1]: {temp[j-1]} - temp[j]: {temp[j]}")
        if temp[j-1] == temp[j]:
            return False
    return True


if __name__ == '__main__':
    nums = [5, 2, 3, 4, 1, 4]
    print(unique1(nums))
    print(unique2(nums))
