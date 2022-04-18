class Vector:
    """
    Represent a vector in a multidimensional space.
    """

    def __init__(self, d):
        """
        Create a vector of d dimensions.
        """
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __add__(self, other):
        """
        Return sum of two vectors.
        """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        # start with vector of zeroes
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        """
        Rely on existing __eq__
        """
        return not self == other
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == '__main__':

    v = Vector(5)
    v[0] = 1
    v[1] = 3
    v[2] = 5
    print(v)

    list_vector = [1, 3, 5, 2, 2]
    print(v + list_vector)

    print(len(v))
