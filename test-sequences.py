def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


if __name__ == '__main__':
    # x = int(input("Enter a number\n"))
    x = 5

    print("fibo with recursion")
    seq = []
    for num in range(x):
        seq.append(fib(num))
    print(seq)

    obj = MyClass()
    print(obj.method())
    print(MyClass.classmethod())
    print(MyClass.staticmethod())
