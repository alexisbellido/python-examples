from time import time, process_time

"""
Running with timeit, which is better than the time module.

python -m timeit '"-".join(str(n) for n in range(100))'

python  -m timeit '"-".join([str(n) for n in range(100)])'

python -m timeit '"-".join(map(str, range(100)))'
"""

def measure_by_wall_clock(iterations):
    """
    The time.time function measures relative to wall clock so it's accuracy will
    depend on what other processes are running on the computer.
    It returns a value in seconds.
    """

    start_time = time()
    print(f"Running {iterations} iterations...")
    for i in range(iterations):
        pass
    end_time = time()
    elapsed = end_time - start_time
    print(f"Elapsed time.time: {elapsed}\n")

def measure_by_process_time(iterations):
    """
    Return the value (in fractional seconds) of the sum of the system and
    user CPU time of the current process.
    """

    start_time = process_time()
    print(f"Running {iterations} iterations...")
    for i in range(iterations):
        pass
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"Elapsed time.process_time: {elapsed}\n")

def measure_by_timeit(iterations):
    """
    Return the value (in fractional seconds) of the sum of the system and
    user CPU time of the current process.
    """

    start_time = process_time()
    print(f"Running {iterations} iterations...")
    for i in range(iterations):
        pass
    end_time = process_time()
    elapsed = end_time - start_time
    print(f"Elapsed time.process_time: {elapsed}\n")

if __name__ == '__main__':
    try:
        iterations = int(input("How many iterations?\n"))
    except ValueError:
        iterations = 2000000
    measure_by_wall_clock(iterations)
    measure_by_process_time(iterations)
