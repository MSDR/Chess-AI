import colorama
import board

if __name__ == '__main__':
    colorama.init()
    #print colorama.Style.NORMAL, colorama.Fore.GREEN, 'X'
    board = board.BoardState()
    board.printBoard()
    colorama.deinit()