# Задача 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения
 
a, b, c = int(input('Введите А, В, С: ')),int(input()),int(input())
d = b**2 - 4*a*c
if d>0:
    x1 = (-b + d ** 0.5)/(2*a)
    x2 = (-b - d ** 0.5)/(2*a)
    print(round(x1, 2), round(x2, 2))
elif d == 0:
    x = -b/(2*a)
    print(round(x,2))
else: print('Действительных корней нет')