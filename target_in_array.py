def find_target(arr, target):
  if target not in arr:
    return [-1, -1]

  i = 0
  while i < len(arr):
    # print(i, arr[i])
    if arr[i] == target:
      break
    i += 1

  print('--------')

  j = len(arr) - 1
  while j >= 0:
    # print(j, arr[j])
    if arr[j] == target:
      break
    j -= 1

  return [i, j]

def find_target_2(arr, target):
  for i in range(len(arr)):
    # print(i, arr[i])
    if arr[i] == target:
      start = i
      while i + 1 < len(arr) and arr[i + 1] == target:
        i += 1
      return [start, i]
  return [-1, -1]

  # print('--------------')

  # for j in range(len(arr) - 1, -1, -1):
  #   print(j, arr[j])


if __name__ == '__main__':
  arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
  target = 5

  # should return [2, 6]
  print(find_target(arr, target))

  print(find_target_2(arr, target))
