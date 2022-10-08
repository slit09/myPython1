def myIst():
    print('''             ╭━━━━╮╲╱╭━━━━╮
             ┃╲╲╲╲┃╭╮┃╱╱╱╱┃
             ╰┈┈┈┈┃┣┫┃┈┈┈┈╯
             ╭╯╱╱╱┃┃┃┃╲╲╲╰╮
             ┃╱╱╱╱┃┃┃┃╲╲╲╲┃
             ╰━━━━╯╰╯╰━━━━╯ ******** ДОБРО ПОЖАЛОВАТЬ В ПОКЕР *****  ╭━━━━╮╲╱╭━━━━╮
                                                                     ┃╲╲╲╲┃╭╮┃╱╱╱╱┃
                                                                     ╰┈┈┈┈┃┣┫┃┈┈┈┈╯
                                                                     ╭╯╱╱╱┃┃┃┃╲╲╲╰╮
                                                                     ┃╱╱╱╱┃┃┃┃╲╲╲╲┃
                                                                     ╰━━━━╯╰╯╰━━━━╯''')
    print()
    print('''                                  версия данной игры 1.1                         ''')
    
myIst()
import random
import sys

def help():
    print("\nСписок команд")
    print("b - сделать ставку;")
    print("с - взять кредит;")
    print("t - бросок кубиков;")

credit = 0
bank = 0
bet = int(0)

print("Для вывода списка команд нажмите введите h")

while True:
    
    print("\nДенег: ", credit)
    print("Ставка: ", bet)
    command = input("Введите команду: ")
    
    if command == 'x':
        sys.exit()
    elif command == 'h':
        help()
    elif command == 'c':
        credit = input("Введите сумму кредита: ")
        credit = int(credit)
        print("Ваши текущие деньги: ", credit,"$")
    elif command == 'b':
        bet = input("Введите ставку: ")
        bet = int(bet)
        if bet > credit:
            print("У вас нет столько.")
            bet = 0
        else:
            credit = credit - bet
    elif command == 't':
        if bet == 0:
            print("Задайте ставку.")
        else:
            val1 = random.randrange(1,6)
            val2 = random.randrange(1,6)
            sum1 = val1 + val2
            print("\nВыпало у человека: ",sum1)
            val1 = random.randrange(1,6)
            val2 = random.randrange(1,6)
            sum2 = val1 + val2
            print("Выпало у компа: ",sum2)
            if sum1 == sum2:
                print("Делайте новый бросок.")
            elif sum1 > sum2:
                credit = credit + bet * 2
                bet = 0
                print("\nВы выиграли!")
            elif sum1 < sum2:
                bet = 0
                print("\nВы проиграли...")
    else:
        print("\nНеизвестная команда")