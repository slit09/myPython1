#viselica01
import random
from traceback import print_tb
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
     ===''','''
  +---+
 [0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\] |
 / \  |
     ===''']

     
words = { 'животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума скунс собака сова тигр тюлень утка хорек черепаха ястреб ящерица'.split(),
          'обьекты':' фонарь ноутбук машина гантеля круг овал квадрат линолиум '.split(),
          'еда':'гамбургер шаурма салат опельсин'.split()}

def getRandomWord(wordList):
    # Эта функция возвращает случайную строку из переданного списка.
    worlkey = random.choice(list(wordList.keys()))

    wordIndex = random.randint(0,len(wordList[worlkey])-1)
    return [wordList[worlkey][wordIndex],worlkey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end=' ' )
    print()

def getGuess(alreadyGuessed):
    # возвращает букву, введенную игроком. Эта функция проверяет, что игрок вве только одну букву и ничего больше
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    # Эта функция возвращает True, если игрок хочет сыграть заново, в противном False
    print('Хотите сыграть еще? (да или нет).')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False
        else:
            print('''Я вас не понял! 
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения игры''')

def vyborS():
    print('Ведите "л" чтобы выбрать легкий режим')
    print('Ведите "c" чтобы выбрать средний режим')
    print('ведите "т" чтобы выбрать хард режим' )
    while True:
        us = input().upper()
        if len(us) != 1:
            print('Введите одну букву')
        elif us not in 'ЛСТ':
            print('''Введите уровень сложности.Введите "Л" для легкого уровня,"C" для среднего уровня,"Т" для хард уровня''')
        else:
            return us

def delV(vybS,hangP):
    if vybS == 'С':
        del HANGMAN_PICS[10]
        del HANGMAN_PICS[9]
    elif vybS == 'Т':
        del HANGMAN_PICS[10]
        del HANGMAN_PICS[9]
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
hm = HANGMAN_PICS

bs = vyborS()
delV(bs,hm)

errorB = ''
yesB = ''
sicretS,keyS = getRandomWord(words)
gameOver = False

while True:
    print(keyS)
    if keyS == "Л":
        print('категории:'+keyS)
    displayBoard(errorB,yesB,sicretS)

    bukva = getGuess(errorB+yesB)

    if bukva in sicretS:
        yesB = yesB + bukva
   
        vseBukvy = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                vseBukvy = False
                break

        if vseBukvy:
            displayBoard(errorB,yesB,sicretS,hm)
            print('Поздравляю.Вы отгодали слово за '+str(len(yesB+errorB))+' количество ходов')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(HANGMAN_PICS)-1:
            displayBoard(errorB,yesB,sicretS)
            print('вы проиграли.Секретное слово: '+sicretS)
            gameOver = True

    if gameOver:
        if playAgain():
            bs = vyborS()
            delV(bs)

            errorB = ''
            yesB = ''
            sicretS,keyS = getRandomWord(words)
            gameOver = False
        else:
            break