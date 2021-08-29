x = input()
1234
x
'1234'
list(x)
['1', '2', '3', '4']
x = list(x)
x[0]
'1'
if int (x[0]) + int (x[1]) == int (x[2]) + int (x[3]):
    print('A happy ticket')
else:
    print('Not a happy ticket')


x = input()
100001
y = x[::-1]
if int(x[0, 1, 2]) == int(x[3, 4, 5]):
    print('Palindrom')
elif x == y
    print('Palindrom')
else:
    print('Not a palindrom')

import math

print("Введите координаты точки и радиус круга")
x_point = float(input("x = "))
y_point = float(input("y = "))
r_circle = float(input("R = "))

hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

if hypotenuse <= r_circle:
    print("Точка принадлежит кругу")
else:
    print("Точка НЕ принадлежит кругу")

