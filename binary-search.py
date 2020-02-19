def binary search(data, target, low, high):
    """
    Return true if target is found in the indicated portion of the list.
    Search only considers portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2 # floor division

if __name__ == '__main__':
    x = int(input("Enter a number\n"))
    print(factorial(x))
