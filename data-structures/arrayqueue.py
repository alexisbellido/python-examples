class Empty(Exception):
    """
    Error attempting to access an element from an empty stack.
    """
    pass


class ArrayQueue:
    """
    FIFO queue implementation using a Python list as the
    underlying storage. Note modulo operations are always against
    the size, the capacity, of this list, not the number of elements in the queue.
    Using a Python list in circular fashion with modular arithmetic.
    """
    # test with a small number but should be bigger in practice
    DEFAULT_CAPACITY = 3

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        """
        remove and return first element of the queue (FIFO)
        initial implementation never shrinks the underlying array
        pronounced like the abbreviation "D.Q."
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        # use module to advance in array in a circular way
        self._front = (self._front + 1) % len(self._data)
        # print('self._size=', self._size)
        # print('len(self._data) =', len(self._data))
        # print('len(self._data) // 4 =', len(self._data) // 4)
        # reduce the array to half of its current size
        # whenever the number of elements stored falls below one fourth of its capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._size -= 1
        return answer
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) # double the array size
        # use modulo, front index and size (number of used elements in array) to calculate
        # the next available position
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def _resize(self, cap):
        """assume cap >= len(self)"""
        # keep existing list
        old = self._data
        # allocate list with new capacity
        self._data = [None] * cap
        # walk over existing list (using module for circular walk) and realign indices in new list
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0 # new resized list will have front at zero

if __name__ == "__main__":
    q = ArrayQueue()

    q.enqueue(2)
    print(q._data)

    q.enqueue(4)
    print(q._data)

    q.enqueue(3)
    print(q._data)

    print('dequeue', q.dequeue())
    print(q._data)

    print('len(q)', len(q))

    print('first', q.first())

    print('dequeue', q.dequeue())
    print(q._data)

    q.enqueue(7)
    print(q._data)

    q.enqueue(9)
    print(q._data)

    print('first', q.first())

    q.enqueue(2)
    print(q._data)

    q.enqueue(4)
    print(q._data)

    q.enqueue(3)
    print(q._data)

    q.enqueue(11)
    print(q._data)

    q.enqueue(13)
    print(q._data)

    print('first', q.first())

    print('dequeue', q.dequeue())
    print(q._data)
    print('dequeue', q.dequeue())
    print(q._data)
    print('dequeue', q.dequeue())
    print(q._data)
    print('dequeue', q.dequeue())
    print(q._data)
    print('dequeue', q.dequeue())
    print(q._data)

    print('dequeue', q.dequeue())
    print(q._data)
    print('dequeue', q.dequeue())
    print(q._data)
    print('dequeue', q.dequeue())
    print(q._data)

    print('len(q)', len(q))




