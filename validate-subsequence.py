def validate_subsequence(seq, subseq):

  # note tnat this exercise requires seq and subseq in the same order
  
  # len(m) = n, len(seq) = m
  # worst case takes O(n x m)
  # for n in subseq:
  #   if n not in seq:
  #     return False

  # return True

  # time complexity
  # https://wiki.python.org/moin/TimeComplexity
  # https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations

  # intersecting sets

  set_seq = set(seq)
  set_subseq = set(subseq)

  return set_seq.intersection(set_subseq) == set_subseq


if __name__ == '__main__':

  seq = [5, 1, 22, 25, 6, -1, 8, 10]
  subseq = [1, 6, -1, 10]

  # seq = [1, 2, 3, 4]
  # subseq = [2, 7]
  # subseq = [2, 4]

  print(validate_subsequence(seq, subseq))
