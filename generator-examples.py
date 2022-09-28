if __name__ == '__main__':
  
  # https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html

  # list comprehension syntax is signiﬁcantly faster than building the list by repeatedly appending

  # generator comprehension
  even_gen = (i for i in range(5) if i % 2 == 0)
  odd_gen = (i for i in range(5) if i % 2 != 0)

  print(list(odd_gen))

  for num in even_gen:
    print(num)

  # a generator can be fed to any function that takes an iterable
  print(sum(1/n for n in range(1, 101)))

  document = "wolf horse ? $ store house ! * extension"

  letters_1 = ' '.join([c for c in document if c.isalpha( )])
  print(letters_1)

  # Better yet, we can entirely avoid the temporary list with a generator comprehension:
  letters_2 = ' '.join(c for c in document if c.isalpha( ))
  print(letters_2)
