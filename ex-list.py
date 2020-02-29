from time import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def get_elapsed(start_time):
    return ((time() - start_time) * 1000)

if __name__ == '__main__':
    # x = int(input("Enter a number\n"))
    # print(factorial(x))
    # compare running times of list operations

    # for i in range(10000000):
    #     pass

    n = 10000000
    data = list(range(n))

    print(f'Lists tests starting with {n:,} elements in data')

    start_time = time()
    print('5 in data', 5 in data)
    print(f"Elapsed milliseconds: {get_elapsed(start_time)}\n")

    start_time = time()
    print('9999995 in data', 9999995 in data)
    print(f"Elapsed milliseconds: {get_elapsed(start_time)}\n")

    start_time = time()
    print('-5 in data', -5 in data)
    print(f"Elapsed milliseconds: {get_elapsed(start_time)}\n")

    # extend method is faster than repeated calls to append because extend is
    # implemented natively in a compiled language; it's a single function call
    # that accomplishes all the work, versus many individual function calls; and
    # it's able to calculate the resulting size of the updated list in advance
    data_for_append = list(range(1000000))
    data_for_extend = list(range(1000000))

    start_time = time()
    for element in data:
        data_for_append.append(element)
    print(f"Using append takes {get_elapsed(start_time)} ms\n")

    start_time = time()
    data_for_extend.extend(data)
    print(f"Using extend takes {get_elapsed(start_time)} ms\n")

    # list comprehension syntax is significantly faster than building
    # the list by repeatedly appending
    start_time = time()
    squares_with_append = []
    for k in data:
        squares_with_append.append(k*k)
    print(f"squares using append takes {get_elapsed(start_time)} ms\n")

    start_time = time()
    squares_with_comprehension = [k*k for k in data]
    print(f"squares using list comprehension takes {get_elapsed(start_time)} ms\n")

    # initialize a list of constant values using [0]*n to produce a list
    # of length n with all values equal to zero is faster than using append
    start_time = time()
    new_with_append = []
    for k in range(n):
        new_with_append.append(0)
    print(f"initialize with append takes {get_elapsed(start_time)} ms\n")

    start_time = time()
    new_with_multiply = [0]*n
    print(f"initialize with [0]*n takes {get_elapsed(start_time)} ms\n")
