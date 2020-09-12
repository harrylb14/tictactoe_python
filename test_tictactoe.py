from game import Game
import numpy as np

class Tests:

  def test_empty_board(self):
    game = Game()
    board = game.board
    assert(board.state == [["-","-","-"],
                           ["-","-","-"],
                           ["-","-","-"]]).all()

  def test_playerX_go(self):
    game = Game()
    board = game.board
    player = game.player1
    player.move(0,0)
    assert(board.state == [["X","-","-"],
                           ["-","-","-"],
                           ["-","-","-"]]).all()
    assert game.turn == "PlayerO"
  
  def test_playerY_go(self):
    game = Game()
    board = game.board
    player1 = game.player1
    player2 = game.player2

    player1.move(0,0)
    player2.move(0,1)
    assert(board.state == [["X","O","-"],
                           ["-","-","-"],
                           ["-","-","-"]]).all()
    assert game.turn == "PlayerX"

  def test_only_place_on_vacant_square(self, capsys):
    game = Game()
    player1 = game.player1
    player2 = game.player2

    player1.move(0,0)
    player2.move(0,0)
    out, err = capsys.readouterr()
    assert "Square not vacant\n" in out
    assert game.turn == "PlayerO"

  def test_can_only_go_on_your_move(self, capsys):
    game = Game()
    player2 = game.player2

    player2.move(0,0)
    out, err = capsys.readouterr()
    assert "Square not vacant\n" in out
    
  def test_winner_row(self):
    game = Game()
    game.board.state = [["X","X","X"],
                        ["O","X","O"],
                        ["-","-","-"]]
    assert(game.winner() == "X")

  def test_winner_column(self):
    game = Game()
    game.board.state = [["X","X","O"],
                        ["O","X","O"],
                        ["-","-","O"]]
    assert(game.winner() == "O")

  def test_winner_diagonal(self):
    game = Game()
    game.board.state = [["X","X","O"],
                        ["O","X","O"],
                        ["-","-","X"]]
    assert(game.winner() == "X")

  def test_game_in_progress(self):
    game = Game()
    game.board.state = [["X","X","O"],
                        ["O","X","O"],
                        ["-","-","-"]]
    assert(game.winner() == "Game in progress")

  def test_over_no_winner(self):
    game = Game()
    game.board.state = [["O","X","O"],
                        ["O","X","O"],
                        ["X","O","X"]]
    assert(game.winner() == "No winner")
