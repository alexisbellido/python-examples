import time
from store import Store

if __name__ == "__main__":

    num = int(input("Enter a number\n"))
    print(f"Storing {num:,} keys...")
    start_time = time.time()

    for i in range(num):
        Store.set(f'num-{i}', i)
        # print(Store.set(f'num-{i}', i))

    end_time = time.time()
    elapsed = (end_time - start_time) * 1000
    print(f'Keys stored: {num:,}')
    print(f'Milliseconds per key: {elapsed/num}')
