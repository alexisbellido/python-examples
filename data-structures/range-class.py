class Range:

    def __init__(self, start, stop=None, step=1):
        """
        Semantics similar to built-in range.

        Python provides automatic iterator implementation for any
        class that deﬁnes both len and getitem.
        """

        if step == 0:
            raise ValueError('step cannot be zero.')
        
        if stop is None:
            start, stop = 0, start

        # use these for __getitem__
        self._start = start
        self._step = step

        if step > 0:
            step_back = -1
        else:
            step_back = 1
        self._length = max(0, (stop - start + step + step_back) // step)

    def __len__(self):
        return self._length
    
    def __getitem__(self, k):

        # if index k is negative turn -k into len(self) - k 

        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step
        

def range_len(start, stop, step):
    if step > 0:
        step_back = -1
    else:
        step_back = 1

    return max(0, (stop - start + step + step_back ) // step)

if __name__ == '__main__':

    r1 = Range(3)
    # print(len(r1))
    for x in r1:
        print(x)

    print('--')
    r2 = Range(7, -3, -1)
    print('len r2', len(r2))
    for index, value in enumerate(r2):
        print(index, value)

    # k = 6 is equivalent to k = -4 because of conversion to len(self) - k
    print(r2[6], r2[-4])


    # print(range_len(0, 4, 1))
    # print(range_len(1, -3, -1))
    # print(range_len(7, 1, -1))
    # print(range_len(7, -3, -1))
    # print(range_len(7, 6, -1))
    # print(range_len(-4, 3, 1))
    # print(range_len(-4, 3, 2))



