def binary_search(data, target, low, high):
    """
    Return true if target is found in the indicated portion of the list.
    Search only considers portion from data[low] to data[high] inclusive.
    Using recursion.
    """
    print("================================")
    print(f"Looking for {target}")
    if low > high:
        return False
    else:
        mid = (low + high) // 2 # floor division
        print("mid: {mid} - data[{mid}]: {num}".format(mid=mid, num=data[mid]))
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            print(f"{target} is on the left, new low: {low}, new high: {mid -1}")
            return binary_search(data, target, low,mid - 1)
        else:
            # recur on the portion right of the middle
            print(f"{target} is on the right, new low: {mid+1}, new high: {high}")
            return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
    target = int(input("Enter a target number\n"))
    data = [1,4,5,6,8,10,13,20,21,24,27,29,33,36,41,43,50,61]
    low = 0
    high = len(data)
    print(binary_search(data, target, low, high))
    print(f"initial low: {low} - initial high: {high}")
    print('initial list', data)
