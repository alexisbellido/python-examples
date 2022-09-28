import functools

def find_longest_words_2(words):
  # with functional programming
  # https://docs.python.org/3/library/functools.html#functools.reduce
  longest_word = functools.reduce(
    lambda longest_word, current_word: longest_word if len(longest_word) > len(current_word) else current_word,
    words
  )
  # not using the third argument, the initializer, as reduce will take the first element by default
  return longest_word

def find_longest_words_1(words):
  # with a loop
  # longest_word = ''
  # for word in words:
  longest_word = words[0]
  for current_word in words[1:]:
    if len(current_word) > len(longest_word):
      longest_word = current_word

  return longest_word

def check_contains(string_list, larger_string):
  # simple loop, O(n^2)
  for word in string_list:
    if word in larger_string:
      return True
  return False

def check_contains_2(string_list, larger_string):
  # using set, O(n) to create two sets and uses a little more space
  intersection = set(string_list).intersection(larger_string.split())
  return len(intersection) > 0

def remove_duplicates(words):
  no_dupes = []
  for word in words:
    if word not in no_dupes:
      no_dupes.append(word)
  return no_dupes

def remove_duplicates_2(words):
  no_dupes_set = set(words)
  return list(no_dupes_set)

def fizzbuzz(numbers):
  # I should replace, not create a new list
  for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
      numbers[i] = 'fizzbuzz'
    elif numbers[i] % 3 == 0:
      numbers[i] = 'fizz'
    elif numbers[i] % 5 == 0:
      numbers[i] = 'buzz'
  return numbers

def fizzbuzz_2(numbers):
  for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
      numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
      numbers[i] = 'fizz'
    elif num % 5 == 0:
      numbers[i] = 'buzz'
  return numbers

def get_animal_age(animal):
  return animal['age']

if __name__ == '__main__':

  numbers = [9, 20, 4, 1, 7, 5, 25, 15, 6, 30]
  print(numbers)
  print(fizzbuzz(numbers))
  print("\n================\n")

  numbers = [9, 20, 4, 1, 7, 5, 25, 15, 6, 30]
  print(numbers)
  print(fizzbuzz_2(numbers))

  print("\n================\n")

  animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
  ]

  animals_by_age = sorted(animals, key = lambda animal: animal['age'], reverse=True)
  print(animals_by_age)
  print("\n================\n")

  animals_by_age_2 = sorted(animals, key = get_animal_age)
  print(animals_by_age_2)
  print("\n================\n")

  # words = [
  #   'cat',
  #   'dog',
  #   'octopus',
  #   'horse',
  # ]

  # longest_word = find_longest_words_1(words)

  # print(words)
  # print(longest_word)

  # longest_word_2 = find_longest_words_2(words)
  # print(longest_word_2)

  # larger_string = 'the horse came to my house'
  # larger_string_2 = 'the bird never came'
  # print(check_contains(words, larger_string))
  # print(check_contains_2(words, larger_string))

  # print("\n================\n")

  # words = ['hello', 'morning', 'roof', 'roof', 'eagle']
  # print(remove_duplicates(words))
  # print(remove_duplicates_2(words))

  # print("\n================\n")

