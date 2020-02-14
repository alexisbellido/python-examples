from time import time

# TODO
# https://stackoverflow.com/questions/2701173/most-efficient-way-for-a-lookup-search-in-a-huge-list-python

def main():
    try:
        iterations = int(input("How many iterations?\n"))
    except ValueError:
        iterations = 25000000
    start_time = time()
    print(f"Running {iterations} iterations...")
    for i in range(iterations):
        pass
    end_time = time()
    elapsed = end_time - start_time
    print(f'Elapsed time: {elapsed}')


if __name__ == '__main__':
    main()
