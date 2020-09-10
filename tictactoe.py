
class Game:
  def __init__(self):
    self.board = Board()
    self.player1 = PlayerX(self, self.board)
    self.player2 = PlayerO(self, self.board)
    self.turn = "PlayerX"
    self.game_over = False

  def winning_player(self):
    if sum(x.count('X') for x in self.board) > sum(x.count('O') for x in self.board):
      return("X")
    else:
      return("O")

  def winner(self):
    if self.board[0][0] == self.board[0][1] == self.board[0][2] != '-' or self.board[1][0] == self.board[1][1] != '-' == self.board[1][2] or self.board[2][0] == self.board[2][1] == self.board[2][2] != '-':
      return(self.winning_player())
    elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '-' or self.board[0][1] == self.board[1][1] == self.board[2][1] != '-' or self.board[0][2] == self.board[1][2] == self.board[2][2] != '-':
      return(self.winning_player())
    elif self.board[0][0] == self.board[1][1] == self.board[2][2] != '-' or self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
      return(self.winning_player())
    elif sum(x.count('-') for x in self.board) == 0:
      return("No winner")
    else:
      return("Game in progress")
  
  
class Board:
  def __init__(self):
    self.state = [["-","-","-"],
                  ["-","-","-"],
                  ["-","-","-"]]

class PlayerX:
  def __init__(self, game, board):
    self.game = game 
    self.board = board

  def move(self, board, column, row):
    if board.state[column][row] == "-" and self.game.turn == "PlayerX":
      board.state[column][row] = "X" 
      print(board.state)
      self.game.turn = "PlayerO"
    else:
      print("Square not vacant")

class PlayerO:
  def __init__(self, game, board):
    self.game = game 
    self.board = board

  def move(self, board, column, row):
    if board.state[column][row] == "-" and self.game.turn == "PlayerO":
      board.state[column][row] = "O" 
      print(board.state)
      self.game.turn = "PlayerX"
    else:
      print("Square not vacant")