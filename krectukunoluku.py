#krestuk noluk

#----------------------------------------------
#раздел импортных модулей
#----------------------------------------------
from ast import Return
from os import POSIX_FADV_SEQUENTIAL, posix_spawn
import random
from re import X
import re
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

def makeMove(board,letter,move):
    board[move] = letter

def golgirwer(bo,it):

    return((bo[7]==it and bo[8]==it and bo[9]==it) or
       (bo[4]==it and bo[5]==it and bo[6]==it) or
       (bo[1]==it and bo[2]==it and bo[3]==it) or
       (bo[7]==it and bo[4]==it and bo[1]==it) or
       (bo[8]==it and bo[5]==it and bo[2]==it) or 
       (bo[9]==it and bo[6]==it and bo[3]==it) or
       (bo[7]==it and bo[5]==it and bo[3]==it) or
       (bo[9]==it and bo[5]==it and bo[1]==it))
def getBoardCopy(board):
    BoardCopy = []
    for i in board:
        BoardCopy.append(i)
    return BoardCopy

def isSpaceFree(board,move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
          print('Ваш следующий ход? Введите номер ячейки.(1-9)')
          move = input()
          return int(move)
          
def cholrasrtMoveFRomlist(board,movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:   
                return None
         
#----------------------------------------------
#основное тело программы
#----------------------------------------------
board = [' ']*10
ml = [1,3,7,9]
displayBoard(board)
hod = cholrasrtMoveFRomlist(board,ml)
#
displayBoard(board)

board[1] = 'X'
board[7] = 'X'
board[9] = 'X'
hod = cholrasrtMoveFRomlist(board,ml)
#
displayBoard(board)

