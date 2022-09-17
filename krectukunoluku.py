#krestuk noluk

#----------------------------------------------
#раздел импортных модулей
#----------------------------------------------
from ast import Return
import random
from re import X
#----------------------------------------------
#раздел созданных функций
#----------------------------------------------
def displayBoard(board):

    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def inputPlayletter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('''выберите X или O на англиском ''')

        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']
def whoGoesfirs():
    if random.randint(0,1) == 0:

        return 'Компьюкхтаррррр'
    else:
        return 'микрочелл' 

def golginwey(board,letter,move):
    board[letter] = move
#----------------------------------------------
#основное тело программы
#----------------------------------------------
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
displayBoard(board)
board[1] = 'O'
board[5] = 'X'
board[9] = 'O'
displayBoard(board)