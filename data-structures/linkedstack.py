class LinkedStack:
    """
    LIFO stack implementation using a singly linked list for storage
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

if __name__ == '__main__':
    pass