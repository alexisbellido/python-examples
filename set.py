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
    n = int(input("Enter a number to search for\n"))

    list = [
        1,2,3,4,5,6,7,8,9,10,11,15,
        1,2,3,4,5,6,7,8,9,10,11,15,
    ]

    start_time = process_time()
    print(lookup_list(n, list))
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"lookup_list {elapsed}")

    start_time = process_time()
    print(lookup_set(n, list))
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"lookup_set {elapsed}")

    # set(iterable)
    # >>> myset = set(['a', 'c', 'd', 'a', 'c'])
    # >>> myset
    # {'a', 'd', 'c'}
    # >>> myset.add('x')
    # >>> myset
    # {'x', 'a', 'd', 'c'}
    # # using a string as the iterable
    # >>> myset2 = set('abac')

    # >>> nums = [1,2,3]
    # >>> names = ['mike', 'joe', 'tom']
    # >>> zip(nums, names)
    # <zip object at 0x7f4892715f00>
    # >>> people = zip(nums, names)
    # >>> for person in people:
    # ...   print(person)
    # ...
    # (1, 'mike')
    # (2, 'joe')
    # (3, 'tom')
    # >>> for person in people:
    # ...   print(person)
    # ...
    # >>> people = zip(nums, names)
    # >>> for age, person in people:
    # ...   print(age, person)
