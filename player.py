class Player:
  def __init__(self, game, board, shape):
    self.game = game 
    self.board = board
    self.shape = shape

  def move(self, board, column, row):
    if board.state[column][row] == "-" and self.game.turn == f"Player{self.shape}":
      board.state[column][row] = f"{self.shape}" 
      print(board.state)
      self.game.change_turn()
    else:
      print("Square not vacant")