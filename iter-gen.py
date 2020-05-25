# iterators and generators

def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results

def factors_generator(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k

def factors_generator_2(n):
    """
    only test up to square root of n
    """
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        # special case if n is perfect square
        yield k

class SequenceIterator:
    """an iterator of any sequence type"""

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """return next element or raise StopIteration"""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration() # there are no more elements

    def __iter__(self):
        """by convention an iterator must return itself"""
        return self

if __name__ == '__main__':

    # nums = [2, 4, 6]
    # seq_iter = SequenceIterator(nums)
    # for i in seq_iter:
    #     print(i)

    # n = 20
    # results = factors(n)
    # print(results)

    # # turn generator into list
    # print(list(factors_generator(n)))

    # # loop over generator with automatic next via for loop
    # print('---')
    # for factor in factors_generator(n):
    #     print(factor)

    # # use iter to call values of generator
    # print('---')
    # factors_gen_2 = factors_generator(n)
    # print(next(factors_gen_2))
    # print(next(factors_gen_2))
    # print(next(factors_gen_2))

    # print('---')
    # for factor in factors_generator_2(n):
    #     print(factor)

    # person = {
    #     'name': 'luis',
    #     'age': 48,
    # }

    # for k, v in person.items():
    #     print(k, v)

    # word = 'kitty'
    # for letter in word:
    #     print(letter, ' ', end='')

    # print('==')

    # nums = [1, 3, 5]
    # nums_iterator = iter(nums)

    # print(nums_iterator)
    # print(next(nums_iterator))
    # print(next(nums_iterator))


