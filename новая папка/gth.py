import random
import math
import sys
import time
def newboard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def zactavka(board):
    strOne = '   '
    for i in range(1,6):
        strOne += (' '*9) + str(i)

    print(strOne)
    print('    '+('0123456789'*6))
    print()
    
    for row in range(15):
        if row<10:
            space = ' '
        else:
            space = ''

        boardStr = ''
        for colum in range(60):
            boardStr += board[colum][row]
        
    
        print('%s%s %s %s' %(space,row,boardStr,row))

    print()
    print('    '+('0123456789'*6))
    print(strOne)


def getRandomChes(ches):
    cheslist = []
    while len(cheslist)<=ches:
        newChes = [random.randint(0,59),random.randint(0,14)]
        if newChes not in cheslist:
            cheslist.append(newChes)
        return cheslist



def vopros(tekstBOPROS):
    print(tekstBOPROS)
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('''Я вас не понял !Введите ответ еще раз .''')

     

def IsDSboard(x,y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14



def makeMove(board,cheslist,x,y):
    minimalDist = 100
    for C_x,C_y in cheslist:
        distanwuz = math.sqrt((C_x-x)*(C_x-x)+(C_y-y)*(C_y-y))
        if distanwuz<minimalDist:
            minimalDist=distanwuz
    minimalDist = round(minimalDist)

    if minimalDist == 0:
        cheslist.remove([x,y])
        print('Вы нашли сундук с сокровищами на затонувшем корабле!')
        return True
    else:
        if minimalDist<10:
            board[x][y] = str(minimalDist)
            print('Сундук с сокровищами был обнаруженна растоянии %s единиц от гидролокатора.' % (minimalDist))
            return False 
        else:
            board[x][y] = 'X'
            print('гидролокатор не обнаружен ')
            return False



def redaktirovanie(preHoda):
    print('''Где следуетопустить гидролокатор?
    (Координаты 0-59 0-14)
    (Или введите "выход" для прекращение игры)''')
    while True:
        move = input()
        if move.lower() == 'Выход':
            print('Спасибо за игру.')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and IsDSboard(int(move[0]),int(move[1])):
            if [int(move[0]),int(move[1])] in preHoda:
                print('Здесь вы уже оп