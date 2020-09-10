from tictactoe import *
class Tests:
  def test_empty_board(self):
    board = Board()
    assert board.state == [["-","-","-"],
                           ["-","-","-"],
                           ["-","-","-"]]