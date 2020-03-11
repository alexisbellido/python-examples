from time import process_time

def lookup_set(x, numbers):
    numbers_set = set(numbers)
    if x in numbers_set:
        return True
    return False

if __name__ == '__main__':
    # n = int(input("Enter a number to search for\n"))

    input = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    start_time = process_time()
    for x in range(10000):
        pass
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"elapsed {elapsed}")
