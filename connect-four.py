import numpy

class Game:
    # Initialize the game.
    def __init__(self, width, height):
        self.board = [] # Used to store the board state, and array of arrays
        self.rows = width
        self.columns = height
        self.filler = ' ' # Value used to display empty slots in the board

        for column in range(self.columns): # Constructs the board as arrays in an array. This will get visualized like a matrix/grid
            self.board.append([self.filler] * self.rows)
        
        self.playerTurn = "X" # Base player turn
        self.gameIsOver = False 
        
        self.proposeMove() 
        
    def proposeMove(self):
        if not self.gameIsOver:
            self.printBoard() # Displays board in terminal
            move = int(input("What row will you play? (0-" + str(self.rows-1) + ")")) # Ask for an input from the player
            #Check if in range:
            if move > self.rows-1: # Check if move is valid
                print("Try a another NUMBER")
                self.proposeMove() # If not, rerun function
                return

            self.makeMove(move) # Make the move
    
    def makeMove(self, move):
        # Run trough the matrix, from the buttom up. Place the piece in the lowest empty spot.
        for column in range(self.columns):
            if self.board[-(column+1)][move] == self.filler:
                print("Valid Move")
                self.board[-(column+1)][move] = self.playerTurn
                self.checkFor4() # Hereafter check for four in a row
                self.changePlayer() # Thereafter change player
                return self.proposeMove() # Next move can be made
        print("Move not valid, try another")
        self.proposeMove()    

    def checkFor4(self):
        # Run through the matrix
        for x in range(self.columns):
            for y in range(self.rows):
                if self.board[x][y] == self.playerTurn: # Only check current players pieces
                    # Return a list of all adjacent pieces as the current player, and the direction relative to the checked piece
                    result = self.checkAdjDir(x, y) 
                    if result != []: # Check if there is any adjacent pieces
                        for i in range(len(result)): # Run as many times as there are adjacent pieces
                            xdir = result[i][0]
                            ydir = result[i][1]
                            #Now check for 4 in row
                            # What its doing is its using the adjacent pieces direction, and checking if there are four of the same pieces in that same direction.
                            count = 0
                            for n in range(4):
                                try: # Will get out of index errors  
                                    # Takes the checked pieces coordinates and ads the direction multiplied by how many times we have another piece in a row
                                    if self.board[x+(xdir)*n][y+(ydir)*n] == self.playerTurn:
                                        count += 1
                                        if count >= 4:
                                            self.gameOver(self.playerTurn) # The game is over
                                except:
                                    #print("Out of index in trying to find 4")
                                    pass
                        
                    
    def checkAdjDir(self, x, y):
        adjDirs = [] # Stores the adj directions
        dirs = [[1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, -1], [-1, 1]] # A list of all the 8 possible directions
        for d in dirs: # Run though all 8 directions and check for adj pieces in the respective direction
            try: # Will also get index errors by nature
                if self.board[x+d[0]][y+d[1]] == self.playerTurn:
                    adjDirs.append([d[0], d[1]])
            except:
                # print("out of index")
                pass
        return adjDirs

    def changePlayer(self): # Simply changes player
        if not self.gameIsOver:
            if self.playerTurn == "X":
                self.playerTurn = "O"
            elif self.playerTurn == "O":
                self.playerTurn = "X"
            return print("Now its " + self.playerTurn + "'s move")

    def printBoard(self):
        # Uses numpy to construct the board in a matrix looking way. 
        matrix = numpy.array(self.board)
        print(matrix)

    def gameOver(self, player):
        self.printBoard()
        print("Game over player: " + player + " won!")
        self.gameIsOver = True


newGame = Game(8, 6) # Instansiates the game with a width of 8 and a height of 6.
