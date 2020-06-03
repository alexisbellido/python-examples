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
