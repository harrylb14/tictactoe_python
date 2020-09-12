# Tic Tac Toe Kata

- An exercise used as an introduction to python. 
- A two-player tictactoe game run in python shell. 

### To Run/Test
- clone repo 
- To test: 
```
pytest
```
To run: 
```
python3
import game from Game
```

### Approach 
- Having never used python before, I spent a while researching OOP and Testing in python. I began by installing and setting up pytest, to enable me to utilise TDD. 
- My first class was the Board, which I representated as a two-dimensional array of arrays. 
- I then built up a player class, and a method which allowed the player to alter the composition of the board at a particular index with their respective shape (X or O). Additional constraints were put in place so match the rules of the game (can only put a shape on a vacant space, can only place a shape when it is the player's turn etc).
- The bulk of the work was figuring out a way to determine the winner, and refactoring it such that it wasn't a mass of if...else statements. I believe I found an elegant solution to do so, utilising sets and board rotation. This was good practice to get to grips with what python can do. 

<img src="Screenshot 2020-09-12 at 15.53.31.png">