if __name__ == '__main__':

  #  sets store elements in a manner that allows near-constant-time checks whether a value is in the set or not, unlike lists, which require linear-time lookups
  
  animals = set()
  animals.add('cow')
  animals.add('dog')
  animals.add('cat')
  animals.add('cat')
  animals.add('duck')
  animals.add('duck')
  animals.add('eagle')

  print('animals', animals)

  teams = {'wolf', 'jackal', 'dog', 'eagle'}

  print('teams', teams)

  print('animals union teams')
  print(animals.union(teams))

  print('animals intersection teams')
  print(animals.intersection(teams))
