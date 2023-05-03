class TicTacToe:
    def __init__(self):
        #Make it possible to varry Board Size
        #Vary Amount of players too
        self.board = [[' ', ' ', ' '], [ ' ', ' ', ' '], [ ' ', ' ', ' ']]
        self.player = ('X','O')
        self.playerIter = iter(self.player)
        self.activePlayer = next(self.playerIter)
        self.xSet = set()
        self.oSet = set()

    def turn(self):

        while True:
            self.move = input("What position do you want to put " + self.activePlayer + ": ")    
            try:
                if int(self.move) >= 0 and int(self.move) <= 8:
                    self.position = [int(self.move)//3 , int(self.move)%3]
                    
                    if self.board[self.position[0]][self.position[1]] == ' ':
                        self.board[self.position[0]][self.position[1]] = self.activePlayer
                        
                        if self.activePlayer == self.player[0]:
                            self.xSet.add(int(self.move))
                        elif self.activePlayer == self.player[1]:
                            self.oSet.add(int(self.move))
                        
                        break
                    else:
                        print('That space is occupied, try again')
                else:
                    print("The input value must be a value between 0 and 8 \n")

            except ValueError:
                print("The input value must be a value between 0 and 8 \n")


        try: 
            self.activePlayer = next(self.playerIter)
        
        except StopIteration:
            self.playerIter = iter(self.player)
            self.activePlayer = next(self.playerIter)
        
        print(self)

    def startGame(self):
        while True:
            print(self)
            while self.endGame() == False:
                self.turn()
            startOver = input('Do you want to play again? Y or N \n')
            if startOver.upper() == 'N':
                print('Thanks for playing!')
                break
            else:
                TicTacToe().startGame()
        return

    def endGame(self):
        # Win Conditions for 3x3
        # 012 345 678 036 147 258 048 246
        winCons = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]

        #Win cons for any size; Row: Positions increase by 1; Column: Positions increase by len(Row); Diagonal: Positions increase by len(Row) + 1
        #Number of symbols in a row need to be equal to the smallest dimension of the board
        
        for x in winCons:
            if x.issubset(self.xSet):
                print('X is the winner!')
                return True 
            if x.issubset(self.oSet):
                print('O is the winner!')
                return True
            
        if len(self.xSet) + len(self.oSet) == (len(self.board)*len(self.board[0])):
            print('The game ended in a tie!')
            return True
        
        return False
        
    def __str__(self):
        #Thinking of making it sizable to any board size
        
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
        boardString = ''
        for i, x in enumerate(self.board):
            boardString += '     |'*(len(x)-1) + '     \n'
            for j, y in enumerate(x):
                if len(x) - 1 != j:
                     boardString += '  '+y+'  |'
                else:
                    boardString += '  '+y+'  \n'
            if len(self.board) - 1 != i:
                boardString += '_____|'*(len(x)-1) + '_____\n' 
            else:
                boardString += '     |'*(len(x)-1) + '     \n'  
        return boardString