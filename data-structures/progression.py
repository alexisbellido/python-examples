class Progression:

    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        # If current is set to None the progression ends.
        self._current += 1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        # By convention an iterator returns itself.
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        self._current += self._increment

class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._current *= self._base
    
class FibonacciProgression(Progression):
    """
    A more general Fibonacci progression.
    """

    def __init__(self, first=0, second=1):
        super().__init__(first)  # start progression with first
        self._prev = second - first  # create an initi previous value that will result in the correct second value
    
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':

    print('p1')
    p1 = Progression()

    # for j in range(3):
    #     print(next(p1))

    p1.print_progression(10)

    print('p2')
    p2 = ArithmeticProgression()
    p2.print_progression(10)

    print('p3')
    p3 = ArithmeticProgression(3, 2)
    p3.print_progression(10)

    print('p4')
    p4 = GeometricProgression(2, 3)
    p4.print_progression(10)

    print('p5')
    p5 = FibonacciProgression()
    p5.print_progression(10)

    print('p6')
    p6 = FibonacciProgression(100, 101)
    p6.print_progression(10)
