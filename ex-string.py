from time import time

def get_elapsed(start_time):
    return ((time() - start_time) * 1000)

if __name__ == '__main__':
    # x = int(input("Enter a number\n"))

    n = 10000000
    data = list(range(n))

    print(f'String tests')
    # print(f'String tests starting with {n:,} elements in data')

    start_time = time()
    print('5 in data', 5 in data)
    print(f"Elapsed milliseconds: {get_elapsed(start_time)}\n")
