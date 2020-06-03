# double-ended queue, or deque, which is usually pronounced “deck”

from collections import deque

class Empty(Exception):
    """
    Error attempting to access an element from an empty stack.
    """
    pass


# class ArrayDequeue:
#     pass

if __name__ == "__main__":
    # d = ArrayDequeue()

    d = deque()

    d.appendleft(1)
    d.appendleft(2)
    print(d)

    d.append(5)
    d.append(6)
    print(d)

    d.pop()
    print(d)

    d.popleft()
    print(d)

    d.append(6)
    d.appendleft(0)
    print(d)

    d.rotate(1)
    print(d)



