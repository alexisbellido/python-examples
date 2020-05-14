def fib(n):
    """
    Given a number n, print nth Fibonacci number.
    Time complexity: T(n) = T(n-1) + T(n-2), exponential
    """
    if n < 0: 
        print("Incorrect input") 
    # first Fibonacci number is 0 
    elif n == 0: 
        return 0
    # second Fibonacci number is 1 
    elif n == 1: 
        return 1
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
    # x = int(input("Enter a number\n"))
    x = 8

    print("fibo with recursion")
    seq = []
    for num in range(x):
        seq.append(fib(num))
    print(seq)

    print("fibo with generator")
    fib_seq = fib_with_generator()
    count = 0
    seq_gen = []
    for i in fib_seq:
        seq_gen.append(i)
        count += 1
        if (count == x):
            break
    print(seq_gen)
