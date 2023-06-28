import random

class TicTacToe:
    #Make it possible to varry Board Size | Done
    #Vary Amount of players too | Done
    #Add an option to choose who starts and switch the starting player each round after
    #Add Scoreboard maybe

    def __init__(self, rows = 3, columns = 3, players = ['X','O'] ):
        #Initializes variables for board
        self.board = []

        #Constructs the board which varies in size based on inputs
        self.rows = rows
        self.cols = columns

        for j in range(rows):
            emptyRow = []
            for i in range(columns):
                emptyRow.append(' ')
            self.board.append(emptyRow)

        #Generates a list of wining positions as sets of positions on the board
        self.winCons = self.WinPos(rows, columns)

        #Counter for how many spots on the board are filled
        self.filledBoard = 0
        
        #Player variables
        self.player = players
        random.shuffle(self.player)
        self.playerIter = iter(self.player)
        self.activePlayer = next(self.playerIter)
        
        #List of sets that will contain each players positions on the board
        self.moveSets = []
        for x in self.player:
            self.moveSets.append(set())

    def turn(self):
        #Loops through the code until a valid move has been made
        while True:
            self.move = input("What position do you want to put " + self.activePlayer + ": ")    
            
            #Checks to see if the input is a valid open position on the board
            try:
                if int(self.move) >= 0 and int(self.move) <= (len(self.board)*len(self.board[0])) - 1:
                    #Converts the single position number into a set of coordinates that correlate to a position on the board
                    self.position = [int(self.move)//len(self.board[0]) , int(self.move)%len(self.board[0])]
                    
                    #Checks to see if the space is empty, if yes the active players symbol is entered into the space
                    if self.board[self.position[0]][self.position[1]] == ' ':
                        self.board[self.position[0]][self.position[1]] = self.activePlayer
                        
                        #Enters the position into the active players move set
                        self.moveSets[self.player.index(self.activePlayer)].add(int(self.move))

                        break
                    else:
                        print('That space is occupied, try again')
                else:
                    print("The input value must be a value between 0 and " + str((len(self.board)*len(self.board[0])) - 1) + "\n")

            except ValueError:
                print("The input value must be a value between 0 and " + str((len(self.board)*len(self.board[0])) - 1) + "\n")
        
        self.filledBoard += 1
        print(self)

    def startGame(self):
        #Prints the empty board to start
        print(self)
        
        #Checks if the game has ended. If not, next turn happens
        while self.endGame() == False:
            self.turn()
        
        #Prints when game has ended
        startOver = input('Do you want to play again? Y or N \n')
        
        #Recreates new TicTacToe Object if the entered Y
        if startOver.upper() == 'Y':
            TicTacToe(self.rows, self.cols, self.player).startGame()
            
        else:
            print('Thanks for playing!')
            
        return

    def endGame(self):
        
        #Iterates through the winCon list and checks to see if the active player has a move set that contains winning positions
        for x in self.winCons:
            if x.issubset(self.moveSets[self.player.index(self.activePlayer)]):
                print(self.activePlayer+' is the winner!')
                return True

        
        #Filled board counts the number of turns and if the number is equal to the amount of spaces then the game has ended in a tie    
        if self.filledBoard == (len(self.board)*len(self.board[0])):
            print('The game ended in a tie!')
            return True
        
        #If game has not ended, change active player to next player in the player list
        else:
            try: 
                self.activePlayer = next(self.playerIter)
            
            except StopIteration:
                self.playerIter = iter(self.player)
                self.activePlayer = next(self.playerIter)
            
            return False
        
    def __str__(self):
        """
             |     |
          X  |  O  |  O
        _____|_____|_____
             |     |     
             |     |
        _____|_____|_____
             |     |
             |     |     
             |     |
        """        

        #Prints the board from the self.board list variable
        boardString = ''
        
        #For loop to go through each row
        for i, x in enumerate(self.board):
            #Prints the top line of each row based on the size of the row
            boardString += '     |'*(len(x)-1) + '     \n'
            
            #Prints each value saved in the board variable in the center of the boardspace
            #loops through for each element in the row
            for j, y in enumerate(x):
                #Checks to see if it is the last element in the row so it doesnt print the boundary line on the right
                if len(x) - 1 != j:
                     boardString += '  '+y+'  |'
                else:
                    boardString += '  '+y+'  \n'
            
            #Checks to see if its the last row so it doesnt print the boundary line on the bottom
            if len(self.board) - 1 != i:
                boardString += '_____|'*(len(x)-1) + '_____\n' 
            else:
                boardString += '     |'*(len(x)-1) + '     \n'  
        return boardString
    
    def WinPos(self, rows, columns):
        # Win Conditions for 3x3
        # 012 345 678 036 147 258 048 246
        #[{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]

        winCons = []
        minDim = min(rows, columns)
        
        for i in range(rows):
            for j in range(columns):

                # horizontal winning positions
                if j + minDim <= columns:
                    winCons.append({(i*columns + k) for k in range(j, j+minDim)})
                
                # vertical winning positions
                if i + minDim <= rows:
                    winCons.append({(k*columns + j) for k in range(i, i+minDim)})
                
                # diagonal winning positions (top-left to bottom-right)
                if i + minDim <= rows and j + minDim <= columns:
                    winCons.append({((i+k)*columns + (j+k)) for k in range(minDim)})
                
                # diagonal winning positions (bottom-left to top-right)
                if i >= minDim - 1 and j + minDim <= columns:
                    winCons.append({((i-k)*columns + (j+k)) for k in range(minDim)})

        return winCons
