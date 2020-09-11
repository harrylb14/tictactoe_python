import numpy as np
from player import Player
from board import Board

class Game:
  def __init__(self):
    self.board = Board()
    self.player1 = Player(self, self.board, "X")
    self.player2 = Player(self, self.board, "O")
    self.turn = "PlayerX"
    self.game_over = False

  def checkRows(self, board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

  def checkDiagonals(self, board):
      if len(set([board[i][i] for i in range(len(board))])) == 1:
          return board[0][0]
      if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
          return board[0][len(board)-1]
      return 0

  def checkWin(self, board):
      #transposition to check rows, then columns
      for newBoard in [board, np.transpose(board)]:
          result = self.checkRows(newBoard)
          if result:
              return result
      return self.checkDiagonals(board)


  def winner(self):
    if self.checkWin(self.board) not in [0, "-"]:
      return self.checkWin(self.board)
    elif sum(x.count('-') for x in self.board) == 0:
      return("No winner")
    else:
      return("Game in progress")

  def change_turn(self):
    if self.turn == "PlayerX":
      self.turn = "PlayerO"
    else:
      self.turn = "PlayerX"
