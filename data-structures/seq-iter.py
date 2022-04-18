class SequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            # return self._seq[self._k]
            return f'item: {self._seq[self._k]}'
        else:
            raise StopIteration()
    
    def __iter__(self):
        """
        By convention an iterator must return itself.
        """
        return self

if __name__ == '__main__':

    vowels = ['a', 'e', 'i', 'o', 'u']
    seq_iter = SequenceIterator(vowels)
    
    print(seq_iter)
    print(list(seq_iter))

    seq_iter_2 = SequenceIterator(vowels)

    for item in seq_iter_2:
        print(item)
    
