import colorama, sys
import utils

class BoardState:
    def __init__(self):
        #an 8x8 list of Pieces, where empty squares are filled with default Pieces
        self.board_ = generateStartingBoard()

        #a list of non-default pieces (Pawn, Bishop, etc.)
        self.pieces_ = []
        for row in self.board_:
            for piece in row:
                if(piece.name_ != 'empty'):
                    self.pieces_.append(piece)

        
    # a move parser. updates board_ and pieces_ accordingly
    # - move is a string of the move to execute in algebraic chess notation
    def initiateMove(self, move):
        utils.raiseNotDefined()

    #prints the current board
    def printBoard(self):
        rowNum = 8
        for row in self.board_:
            colNum = 1
            print ""
            print " +---+---+---+---+---+---+---+---+"
            sys.stdout.write(str(rowNum) + "|") #stdout used because print inserts a space at the end of each print
            for piece in row:
                #set background color
                if ((colNum+rowNum)%2==1):
                    print colorama.Back.WHITE,  
                else:
                    print colorama.Back.GREEN,
                
                #set piece color and draw
                if(piece.color_ == 'white'):
                    print colorama.Style.BRIGHT + colorama.Fore.WHITE + piece.icon_ + ' ',
                else:
                    print colorama.Style.DIM + colorama.Fore.BLACK + piece.icon_ + ' ',

                sys.stdout.write(colorama.Back.BLACK + colorama.Style.NORMAL + colorama.Fore.WHITE + "|")
                colNum += 1
            rowNum -= 1
            
        print ""       
        print " +---+---+---+---+---+---+---+---+"
        print "   a   b   c   d   e   f   g   h  "
        print colorama.Back.BLACK #restores background color

    # returns the piece residing in square
    # - square is an (int, int), each between [0, 7]
    def readSquare(self, square):
        x,y = square
        if(not (0 <= x <= 7 and 0 <= y <= 7)):
            utils.raiseError('square out of range of board')

        return self.board_[x][y]

    # creates a generator of next legal BoardStates for a given color
    # - color is either 'white' or 'black'
    def generateSuccessors(self, color):
        utils.raiseNotDefined()
        #for piece in pieces_:
        #   for move in piece.getLegalMoves

    # quantifies how good the board is for a given color
    # - color either 'white' or 'black'
    def evaluateBoard(self, color):
        utils.raiseNotDefined()

class Piece:
    # - position should be an (int, int) between [0, 7]
    # - color either 'black' or 'white'
    def __init__(self, position, color):
        self.name_ = 'empty'
        self.icon_ = ' '
        self.position_ = position
        self.color_ = color

    # returns a generator giving all legal moves for the piece on the board
    def getLegalMoves(self, BoardState):
        return 
        yield

    # given a destination square, checks that a move to that square is legal
    def checkLegality(self, BoardState, destSquare):
        return False #cannot move a non-existant piece

    def __str__(self):
        spacing = ''
        for i in range(7-len(self.name_)):
            spacing += ' ' 
        return self.name_ + spacing + str(self.position_) + ' ' + self.color_

#for specifications of any Piece descendents, refer to Piece
class Pawn(Piece):
    def __init__(self, position, color):
        self.name_ = 'pawn'
        self.icon_ = 'P'
        self.position_ = position
        self.color_ = color

    def getLegalMoves(self, BoardState):
        utils.raiseNotDefined()

    def checkLegality(self, BoardState, destSquare):
        utils.raiseNotDefined()


class Knight(Piece):
    def __init__(self, position, color):
        self.name_ = 'knight'
        self.icon_ = 'N'        
        self.position_ = position
        self.color_ = color

    def getLegalMoves(self, BoardState):
        utils.raiseNotDefined()

    def checkLegality(self, BoardState, destSquare):
        utils.raiseNotDefined()


class Bishop(Piece):
    def __init__(self, position, color):
        self.name_ = 'bishop'
        self.icon_ = 'B'
        self.position_ = position
        self.color_ = color

    def getLegalMoves(self, BoardState):
        utils.raiseNotDefined()

    def checkLegality(self, BoardState, destSquare):
        utils.raiseNotDefined()


class Rook(Piece):
    def __init__(self, position, color):
        self.name_ = 'rook'
        self.icon_ = 'R'
        self.position_ = position
        self.color_ = color

    def getLegalMoves(self, BoardState):
        utils.raiseNotDefined()

    def checkLegality(self, BoardState, destSquare):
        utils.raiseNotDefined()


class Queen(Piece):
    def __init__(self, position, color):
        self.name_ = 'queen'
        self.icon_ = 'Q'
        self.position_ = position
        self.color_ = color

    def getLegalMoves(self, BoardState):
        utils.raiseNotDefined()

    def checkLegality(self, BoardState, destSquare):
        utils.raiseNotDefined()


class King(Piece):
    def __init__(self, position, color):
        self.name_ = 'king'
        self.icon_ = 'K'
        self.position_ = position
        self.color_ = color

    def getLegalMoves(self, BoardState):
        utils.raiseNotDefined()

    def checkLegality(self, BoardState, destSquare):
        utils.raiseNotDefined()


#returns a 2d list of pieces in the standard chess starting position
def generateStartingBoard():
    board = [[Rook((0, 0), 'white'), Knight((1, 0), 'white'), Bishop((2, 0), 'white'), Queen((3, 0), 'white'), King((4, 0), 'white'), Bishop((5, 0), 'white'), Knight((6, 0), 'white'), Rook((7, 0), 'white')]]
    board.append([Pawn((x, 1), 'white') for x in range(8)])
    for y in range(2, 6):
        board.append([Piece((x, y), 'empty') for x in range(8)])
    board.append([Pawn((x, 6), 'black') for x in range(8)])
    board.append([Rook((0, 7), 'black'), Knight((1, 7), 'black'), Bishop((2, 7), 'black'), Queen((3, 7), 'black'), King((4, 7), 'black'), Bishop((5, 7), 'black'), Knight((6, 7), 'black'), Rook((7, 7), 'black')])

    return board