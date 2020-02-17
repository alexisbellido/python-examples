from time import process_time
from bisect import bisect_left

def lookup_set(x, numbers):
    numbers_set = set(numbers)
    if x in numbers_set:
        return True
    return False

def lookup_list(x, numbers):
    if x in numbers:
        return True
    return False

if __name__ == '__main__':
    list = [
        1,2,3,4,5,6,7,8,9,10,11,15,
        1,2,3,4,5,6,7,8,9,10,11,15,
    ]

    start_time = process_time()
    print(lookup_list(15, list))
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"lookup_list {elapsed}")

    start_time = process_time()
    print(lookup_set(20, list))
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"lookup_set {elapsed}")
