print('''Есть управление:
ax+b=0.
Посмотрим чучелу1 равен x при введенных
значенях a и b.''')
a = input('Введите число "a"')
b = input('Введите число "b"')
a = int(a)
b = int(b)

if (a==0 and b==0):
     print('INF')

if (a==0 and b!=0):
    print('NO')

if (a!=0 and b!=0):
    print('NO')

if (a!=0 and b%a!=0):
    n = int(-b/a)
    print(n)