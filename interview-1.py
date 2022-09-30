from math import sqrt
from collections import Counter

def get_primes(start, end):
  print(f'look for primes between {start} and {end}')
  primes = []
  for i in range(start, end + 1):
    if is_prime(i):
      # print(i, 'is prime')
      primes.append(i)
  return primes

def is_prime(n):
  if n <= 1:
    return False

  # check from 2 to sqrt(n)
  # print(n, int(sqrt(n) + 1))
  for i in range(2, int(sqrt(n) + 1)):
    if n % i == 0:
      return False
  return True

def are_anagrams(word_1, word_2):
  """
  two strings are anagrams if they are made of the same
  characters with the same frequencies
  """

  print(word_1, word_2)

  if len(word_1) != len(word_2):
    return False
  
  # counter_1 = Counter(list(word_1))
  # counter_2 = Counter(list(word_2))

  counter_1 = Counter(word_1)
  counter_2 = Counter(word_2)
  
  print('\n-------------------\n')
  print('counter_1')
  print(counter_1)
  print(dict(counter_1))
  print('\n-------------------\n')
  print('counter_2')
  print(counter_2)
  print(dict(counter_2))
  print('\n-------------------\n')

  return counter_1 == counter_2

  # print(sorted(word_1))
  # print(sorted(word_2))
  # return sorted(word_1) == sorted(word_2)


if __name__ == '__main__':

  # n = 39
  # print(f'is {n} prime? {is_prime(n)}')

  # primes = get_primes(100, 200)
  # print(primes)

  print(are_anagrams('garden', 'danger'))

  print('\n-------------------\n')

  print(are_anagrams('xxxgarden', 'dangereri'))

  print('\n-------------------\n')

  print(are_anagrams('garden', 'ostrich'))