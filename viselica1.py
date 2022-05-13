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
eB = 'клмнфу'
yB = 'о'
sS = 'ворон'

displayBoard(eB,yB,sS)
