def fib(n):
    """
    Given a number n, print nth Fibonacci number.
    Time complexity: T(n) = T(n-1) + T(n-2), exponential: O(2^n)
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

# memoization to do it the dynamic programming way where
# we store solutions already calculated
def fib_memo(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result

def fib_bottom_up(n):
    """
    bottom-up approach to do it the dynamic programming way where
    we store solutions already calculated
    """
    bottom_up = []
    bottom_up.append(0)
    bottom_up.append(1)
    bottom_up.append(1)
    print(bottom_up)
    for i in range(3, n):
        bottom_up.append(bottom_up[i - 1] + bottom_up[i - 2])
    return bottom_up

# const fib_bottom_up = n => {
#     if (n < 0) {
#         throw Error("Incorrect input");
#     } else if (n == 0) { 
#         // first Fibonacci number is 0 
#         return 0;
#     } else if (n == 1) {
#         // second Fibonacci number is 1 
#         return 1;
#     }
#     const bottom_up = Array(n + 1);
#     bottom_up[0] = 0;
#     bottom_up[1] = 1;
#     bottom_up[2] = 1;
#     for (let i = 3; i < (n + 1); i++) {
#         bottom_up[i] = bottom_up[i-1] + bottom_up[i-2];
#     }
#     return {
#         fib: bottom_up[n],
#         bottom_up: bottom_up,
#     }
# };

if __name__ == '__main__':
    """n is the number of elements to include in the fibonacci sequence"""
    # n = int(input("Enter a number\n"))
    n = 8

    print("fibo with recursion")
    seq = []
    for num in range(n):
        seq.append(fib(num))
    print(seq)

    print("fibo with generator")
    fib_seq = fib_with_generator()
    count = 0
    seq_gen = []
    for i in fib_seq:
        seq_gen.append(i)
        count += 1
        if (count == n):
            break
    print(seq_gen)

    # // create an array filled with None
    print('=== fibo_memo', n);
    memo = [None] * n
    # memo = [None] * (n + 1)
    fib_memo_list = []
    for i in range(n):
        # print('fib_memo of', i, fib_memo(i, memo))
        fib_memo_list.append(fib_memo(i, memo))
    print(fib_memo_list)

    # creates the array with results from the bottom up inside the function
    print('=== fib_bottom_up', n, fib_bottom_up(n))
