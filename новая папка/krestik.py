#game
import random
def zactavka(board):
    print('Следуйщий ход:')
    print('    ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('    ')

def vibor():
    letter = ''
    while not (letter=='X' or letter=='O'):
        print('напишите по английский X или O для выбора.')

        letter = input().upper()
    
    
    if letter == 'X':
        return['X','O']
    else:
        return['O','X']

def bot(board,computerLetter):
    if computerLetter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'
    
    for i in range(1,10):
        boardcopy = copyrovanie(board)
        if space(board,i):
            idti(boardcopy,computerLetter,i)
            if win(boardcopy,computerLetter):
               return i

    move = hodII(board,[1,3,7,9])
    if move != None:
        return move

    if space(board,5):

        return hodII(board,[2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if space(board,i):
            return False
    return True


def whoGo():
    if random.randint(0,1) == 0:
        return 'компьютер'
    else:
        return 'человек'

def idti(board,letter,move):
    board[move] = letter

def win(bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
    (bo[4]==le and bo[5]==le and bo[6]==le) or
    (bo[1]==le and bo[2]==le and bo[3]==le) or
    (bo[7]==le and bo[4]==le and bo[1]==le) or
    (bo[8]==le and bo[5]==le and bo[2]==le) or
    (bo[9]==le and bo[6]==le and bo[3]==le) or
    (bo[7]==le and bo[5]==le and bo[3]==le) or
    (bo[9]==le and bo[5]==le and bo[1]==le))
def copyrovanie(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def space(board,move):
    return board[move] == ' '

def makemove(board):
    move = ' '
    while move not in ' 1 2 3 4 5 6 7 8 9'.split() or not space(board,int(move)):
        print('ваш ход напишите (1-9)')
        move = input()
    return int(move)

def hodII(board,movesList):
    possibleMoves = []
    for i in movesList:
        if space(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None



print('игра в "КРЕСТИКИ НОЛИКИ"')
while True:
    theBoard = [' ']*10

    playerletter, computerletter = vibor()

    turn = whoGo()
    #turn = 'человек'
    print(''+turn+' ходит первый.')

    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'человек':
            zactavka(theBoard)
            move = makemove(theBoard)
            idti(theBoard,playerletter,move)
        
            if win(theBoard,playerletter):
                zactavka(theBoard)
                print('ты выйграл!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    zactavka(theBoard)
                    print('ничья')
                    break
                else:
                   turn = 'компьютер'
        else:
            zactavka(theBoard)
            move = bot(theBoard,computerletter)
            idti(theBoard,computerletter,move)

            if win(theBoard,computerletter):

                zactavka(theBoard)
                print('компьютер выйграл!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    zactavka(theBoard)
                    print('ничья')
                    break
                else:
                    turn = 'человек'

                    
    print('сыграем еще раз?')
    if not input().lower().startswith('д'):
        break
                                                                                                                                                                                                  �=T��V��e���#m�5��S�I/�K(���U��ʅ[6`�"V�F͊;*�S�5�V��'���Tu�)��`�V����Y�P)��:wtEƙ���kXNK�^����5~��,��Ǆ,�!"�M4�14�Z1�Q*3�SF���[Є}��Be5�u����ZgגOGEW�dDjnM�OK̑9�ys���uE�����lǌ�/$�Id1T���>CC�&Ӄ4#_�����Kg��޹32�4�j=�Da�?�Q&�b��PO�%o���7�ӊ�`�Z�`{U�j�����|�m�\��e���>���Jđ�V��y\(���5����/�LV>\C�<���O����#� ��%Z>V?���碪����RFY�`�4c�:
h�Չ&z(M�D!��ߪ�H�s����V,���P�|��ͪBR���)�w�������U 8I���%��vw�=(U���Ƀ/7yY�{?j��|ڙ/h�
~��<���,����A�����Pb�V��8KW�~V%�����U�e�O��B0|!	@�ˀ4������Yu�P0��j���>  h�0�A +��� ���;�\ƫz�b�a�0����"�`@Vj���R>������0 A�=R�\1��Q(<��� �x��2�QR��?v�'�ω ��8|��C��[?�%T��i�$*���^T���ޥ�����1n/ُVtH�6�����R�)��2M��`����
��T