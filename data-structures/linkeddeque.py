class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """
        nested class, by convention the name starts with underscore to indicate
        it's only used internally; it's not public
        """
        # streamline memory usage by not creating a dictionary except
        # for the listed members
        # https://book.pythontips.com/en/latest/__slots__magic.html
        # https://stackoverflow.com/questions/472000/usage-of-slots
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
                self._element = element
                self._prev = prev
                self._next = next

class LinkedDeque(_DoublyLinkedBase):
    """
    Double-ended queue implementation based on a doubly linked list.
    Note that it inherits from _DoublyLinkedBase.
    """
    pass

if __name__ == '__main__':
    pass