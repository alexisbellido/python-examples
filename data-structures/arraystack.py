class Empty(Exception):
    """
    Error attempting to access an element from an empty stack.
    """
    pass


class ArrayStack:
    """
    LIFO stack implementation using a Python list as the
    underlying storage.
    """

    def __init__(self):
        """
        Create an empty stack.
        """
        self._data = []

    def __len__(self):
        """
        Return the number of elements in the stack.
        This is a Python dunder method.
        """
        return len(self._data)

    def is_empty(self):
        """
        Return True is the stack is empty.
        """
        return len(self._data) == 0

    def get(self):
        """
        Return the underlying list.
        """
        return self._data

    def push(self, e):
        """
        Add element e to the top of the stack.
        """
        self._data.append(e)

    def top(self):
        """
        Also known as peek, which is a more generic term.
        Return, but do not remove, the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

if __name__ == '__main__':
    """
    A stack is a collection of objects that are inserted and removed according to
    he last-in, first-out (LIFO) principle.
    """
    # x = int(input("Enter a number\n"))
    print('Stack')
    S = ArrayStack()
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop())
    print(S.is_empty())
    print(S.pop())
    print(S.is_empty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))
    print('The stack contains', S.get())
    print('---------')

    print('Use ArrayStack to reverse file. Start with animals from bigger to smaller')
    animals_stack = ArrayStack()
    path = 'animals-by-size.txt'
    with open(path) as file:
        for line in file:
            animal = line.strip('\n')
            print('- ', animal)
            animals_stack.push(animal)

    print('Now pop stack to print animals from smaller to bigger')
    while not animals_stack.is_empty():
        print('- ', animals_stack.pop())
