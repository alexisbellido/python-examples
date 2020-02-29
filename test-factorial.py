def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def naive_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


if __name__ == '__main__':
    x = int(input("Enter a number\n"))
    print(factorial(x))
    print(naive_factorial(x))
