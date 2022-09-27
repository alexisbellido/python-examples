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

if __name__ == '__main__':

  words = [
    'cat',
    'dog',
    'octopus',
    'horse',
  ]

  longest_word = find_longest_words_1(words)

  print(words)
  print(longest_word)

  longest_word_2 = find_longest_words_2(words)
  print(longest_word_2)

  larger_string = 'the horse came to my house'
  larger_string_2 = 'the bird never came'
  print(check_contains(words, larger_string))
  print(check_contains_2(words, larger_string))