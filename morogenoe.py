k = input('Ведите количество мозгов,которые хотите купить')
k = int
if k in (1,2,3,4,7):
    print('NO дядя')
else:
    print('YES дядя')
doneGames = 'да'
while doneGames == 'да' or doneGames == 'не надо дядя':
    print('хотите купить еще раз?')
    doneGames = input()
