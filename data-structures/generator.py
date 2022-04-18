def factors_fun(n):
    results = []
    for k in range(1, n + 1):
        if n % k == 0:
            results.append(k)
    return results

def factors_gen(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k

def factors_gen_2(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            print("n: {}, k: {}".format(n, k))
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future

if __name__ == '__main__':
    # factors_as_function = factors_fun(100)
    # print(factors_as_function)

    # for x in factors_gen(100):
    #     print(x)
    
    for x in factors_gen_2(100):
        print(x)

    count = 0
    for x in fibonacci():
        print(x)
        count += 1
        if count == 5:
            break
