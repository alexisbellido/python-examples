class Empty(Exception):
    """
    Error attempting to access an element from an empty stack.
    """
    pass


class LinkedStack:
    """
    LIFO stack implementation using a singly linked list for storage.
    Put top of stack at the head of the linked list as we can insert and
    delete elements from the head in constant time.
    """

    class _Node:
        """
        nested class, by convention the name starts with underscore to indicate
        it's only used internally; it's not public
        """
        # streamline memory usage by not creating a dictionary except
        # for the listed members
        # https://book.pythontips.com/en/latest/__slots__magic.html
        # https://stackoverflow.com/questions/472000/usage-of-slots
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
                self._element = element
                self._next = next

    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        """add element e to top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        """return, without removing, the element at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        """
        Also known as peek, which is a more generic term.
        Return, but do not remove, the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

if __name__ == '__main__':
    ls = LinkedStack()

    print('ls.push(2)')
    ls.push(2)
    print('LinkedStack object', ls)
    print('_Node object at the head of the linked stack',  ls._head)
    print('_element for head', ls._head._element)
    print('_next for head', ls._head._next)

    print('ls.push(4)')
    ls.push(4)
    print('LinkedStack object', ls)
    print('_Node object at the head of the linked stack',  ls._head)
    print('_element for head', ls._head._element)
    print('_next for head', ls._head._next)

    print('size', len(ls))

    top = ls.top()
    print('top = ls.top()')
    print('top', top)

    element = ls.pop()
    print('element = ls.pop()', element)

    element = ls.pop()
    print('element = ls.pop()', element)

    element = ls.pop()
    print('element = ls.pop()', element)
