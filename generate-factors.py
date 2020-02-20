def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            print(f"{k} is a factor of {n}")
            results.append(k)
    return results


def factors_with_generator(n):
    for k in range(1, n+1):
        if n % k == 0:
            print(f"{k} is a factor of {n}")
            yield k


if __name__ == '__main__':
    n = int(input("Enter a number\n"))

    print("regular loop")
    f1 = factors(n)
    print(f1)

    print("using a generator")
    print(list(factors_with_generator(n)))
