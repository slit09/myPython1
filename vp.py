import secrets


HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
     +---+
     0   |
         |
         |
        ===''','''
        +---+
        0   |
        |   |
            |
           ===''','''
        +---+
        0   |
       /|   |
            |
           ===''','''
        +---+
        0   |
       /|\  |
            |
           ===''','''
        +---+   
        0   |
       /|\  |
       /    |
           ===''','''
        +---+
        0   |
       /|\  |
       / \  |
           ===''']

def displayBoard(errorB,yesB,sicretS):
    print(HANGMAN_PICS[len(errorB)])
    print()
    print('Ошибочные буквы:',end=' ')
    print(errorB)
    slovo = '_'*len(sicretS)
    for i in range(len(sicretS)):
        if sicretS[i] in yesB:
            slovo = slovo[0:i]+sicretS[i]+slovo[i+1:]
    print(slovo)


eB = 'аубцфш'
yB = 'еьм'
sS = 'пельмень'

displayBoard(eB,yB,sS)
