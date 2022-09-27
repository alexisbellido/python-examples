if __name__ == '__main__':
  numbers = [1, 2, 3, 4]
  reversed = []

  print(numbers)

  # for i in range(len(numbers)):
  #   last = numbers.pop()
  #   reversed.append(last)

  while len(numbers):
    last = numbers.pop()
    reversed.append(last)

  print(reversed)
