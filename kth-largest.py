def find_k_largest(arr, k):

  print('arr', arr)
  print('k', k)

  # removing the maximum value k - 1 times
  # O(kn), a little bit slow

  # for i in range(k - 1):
  #   arr.remove(max(arr))

  # return max(arr)

  # sorting into a new list
  # sort is O(n log(n)
  sorted_arr = sorted(arr)

  print('sorted_arr', sorted_arr)

  result = sorted_arr[-k]

  return result


if __name__ == '__main__':

  arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
  k = 4

  print('result', find_k_largest(arr, k))
