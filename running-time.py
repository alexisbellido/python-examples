from time import time


def measure_by_wall_clock(iterations):
    """
    The time function measures relative to wall clock.
    """

    start_time = time()
    print(f"Running {iterations} iterations...")
    for i in range(iterations):
        pass
    end_time = time()
    elapsed = end_time - start_time
    print(f'Elapsed time: {elapsed}')


if __name__ == '__main__':
    try:
        iterations = int(input("How many iterations?\n"))
    except ValueError:
        iterations = 20000000
    measure_by_wall_clock(iterations)
