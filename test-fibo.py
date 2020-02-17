def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    seq = []
    x = int(input("Enter a number\n"))
    for num in range(x):
        seq.append(fib(num))
    print(seq)
