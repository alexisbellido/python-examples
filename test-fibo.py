def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib_with_generator():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future

if __name__ == '__main__':
    x = int(input("Enter a number\n"))

    print("fibo with recursion")
    seq = []
    for num in range(x):
        seq.append(fib(num))
    print(seq)

    print("fibo with generator")
    fib_seq = fib_with_generator()
    count = 0
    for i in fib_seq:
        print(i)
        count += 1
        if (count == x):
            break
