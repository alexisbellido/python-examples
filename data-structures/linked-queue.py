class Empty(Exception):
    """
    Error attempting to access an element from an empty stack.
    """
    pass

class LinkedQueue():
    """
    FIFO queue implementation using a singly linked list for storage.
    To perform operations on both ends of the queue we maintain references
    to _head and _tail.
    Put front of the queue at the _head and back of the queue at the _tail
    to dequeue and enqueue in constant time.
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
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """return, but don't remove, the element at the front of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def dequeue(self):
        """remove and return the first element of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None # queue empty, removed head had been the tail
        return answer
    
    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None) # node will be the new tail
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

if __name__ == "__main__":
    lq = LinkedQueue()
    print('lq', lq)