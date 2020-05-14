def binary_search(alist, item):
    """
    Finds the position of a target value within a sorted array.
    Logarithmic complexity.
    The algorithm halves the input every single time it iterates.
    """
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

if __name__ == '__main__':
    target = int(input("Enter a target number\n"))
    data = [1,4,5,6,8,10,13,20,21,24,27,29,33,36,41,43,50,61]
    print(binary_search(data, target))