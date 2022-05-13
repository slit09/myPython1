
from ast import Return
from getopt import error
import random
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
words = 'яблоко,апельсин,огурец'.split()

def getRandomWord (wordlist):
    # Это функция возращает случаюную строку из переданного списка.
    wordIndex = random.randint(0, len(wordlist)-1)
    return wordlist[wordIndex]
def proverkaVvoda(bukEst):
    vvod = input('Введите букву')
    while True:
        n = input()
        n = n.lower()
        if len(n)!=1:
           print('Введите 1 букву')
        elif n in alreadyGuessed:
            print('вы уже называли эту букву.')
        elif n not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите букву')
        else:
           return n

def playAgain():
    #Эта функция возращает True, если игрок хочет сыграть заново, в противном False
    print('Хотите сыграть ещё раз? (да или нет')
    