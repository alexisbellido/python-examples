def fizzBuzz(n):
    # Write your code here
    if 0 < n < 2 * (10 ** 5):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
            elif i % 3 == 0 and i % 5 != 0:
                print('Fizz')
            elif i % 5 == 0 and i % 3 != 0:
                print('Buzz')
            else:
                print(i)
    else:
        # print(f'Not valid for {n}   ')
        return

if __name__ == '__main__':
    # x = int(input("Enter a number\n"))
    # print(x)
    fizzBuzz(15)
    fizzBuzz(-2)
    fizzBuzz(200001)
