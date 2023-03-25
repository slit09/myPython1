import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Вы угадали!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Горячо')
        elif guess[i] in secretNum:
            clues.append('Тепло')
    if len(clues) == 0:
        return 'Холодно'
    
    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num == '':
        return False
    
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
        
    return True

def playAgain(