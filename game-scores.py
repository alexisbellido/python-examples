# using special methods
# https://docs.python.org/3/reference/datamodel.html#special-method-names

class GameEntry:

  def __init__(self, name, score):
    self._name = name
    self._score = score
  
  def get_name(self):
    return self._name

  def get_score(self):
    return self._score

  def __str__(self):
    return f'{self._name}: {self._score}'


class ScoreBoard:

  def __init__(self, capacity=10):
    self._board = [None] * capacity
    self._n = 0  # number of actual entries
  
  def __getitem__(self, key):
    return self._board[key]

  def __str__(self):
    return "\n".join(str(self._board[j]) for j in range(self._n))

  def add(self, entry):
    score = entry.get_score()

    # if board is not full or new score is higher than the last entry
    good = self._n < len(self._board) or score > self._board[-1].get_score()

    if good:
      if self._n < len(self._board):
        self._n += 1
      
      # shift lower scores rightward to make room for new entry
      j = self._n - 1
      while j > 0 and self._board[j-1].get_score() < score:
        self._board[j] = self._board[j-1]
        j -= 1
      self._board[j] = entry


if __name__ == '__main__':
  
  entry_1 = GameEntry('mike', 21)
  entry_2 = GameEntry('joe', 17)
  entry_3 = GameEntry('bill', 125)
  entry_4 = GameEntry('ted', 3)
  entry_5 = GameEntry('bob', 250)

  # print(entry_1)
  # print(entry_2)

  score_board = ScoreBoard(4)
  score_board.add(entry_1)
  score_board.add(entry_2)
  score_board.add(entry_3)
  score_board.add(entry_4)
  score_board.add(entry_5)

  print(score_board)
