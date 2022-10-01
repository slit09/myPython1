#krestuk noluk
import random
from re import M, T
from webbrowser import get
#----------------------------------------------
#раздел импортных модулей
#----------------------------------------------
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

        return 'Компьюкхтаррррр '
    else:
        return 'микрочелл ' 

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

def getcompiterNove(board,computeletter):
    if computeletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(board,i):
            makeMove(boardCopy,computeletter,i)
            if golgirwer(boardCopy,computeletter):
                return i

    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(board,i):
            makeMove(boardCopy,playerletter,i)
            if golgirwer(boardCopy,playerletter):
                return i

    move = cholrasrtMoveFRomlist(board,[1,3,7,9])
    if move != None:
        return move
    if isSpaceFree(board,5):
        return 5
    return cholrasrtMoveFRomlist(board[2,4,6,8])

def isBoardFull(board):
    for i in range (1,10):
        if isSpaceFree(board,i):
            return False
    return True


#----------------------------------------------
#основное тело программы
#----------------------------------------------
print('ИГРА КРЕСТИКИ НОЛИКИ!')
while True:
    theboard = [' ']*10
    playerletter,computeletter = inputPlayletter()
    turn = whoGoesfirs()
    print(''+turn+'ходит первым.')
    gameIsPlaing = True

    while gameIsPlaing:
        if turn == 'микрочелл ':
            displayBoard(theboard)
            move = getPlayerMove(theboard)
            makeMove(theboard,playerletter,move)
            
            if golgirwer(theboard,playerletter):
                displayBoard(theboard)
                print('поздравляю! Ты выйграл!')
                gameIsPlaing = False
            else:
                if isBoardFull(theboard):
                    displayBoard(theboard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьюкхтаррррр '
        else:
            move = getPlayerMove(theboard)
            if isBoardFull(theboard):
                displayBoard(theboard)
                print('Ничья!')
                break
            else:
                turn = 'Компьюкхтаррррр '

    else:
        move = getcompiterNove(theboard,computeletter)
        makeMove(theboard,computeletter,move)
        if golgirwer(theboard,computeletter):
            displayBoard(theboard)
            print('ИИ был сильнее!Вы проиграли-_-')
            gameIsPlaing = False
        else:
            if isBoardFull(theboard):
               displayBoard(theboard)
               print('Ничья!')
               break
            else:
                turn = 'микрочелл '
    print('Сыграем еще раз?(да или нет)')
    if not input().lower().startswith('д'):
        break

