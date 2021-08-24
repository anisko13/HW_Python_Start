Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "123"
>>> int(x)
123
>>> float(x)
123.0
>>> x = 123
>>> str(x)
'123'
>>> float(x)
123.0
>>> x = 123.0
>>> str(x)
'123.0'
>>> int(x)
123
>>> x = 12.345
>>> str(x)
'12.345'
>>> input("Card number ")
Card number 2446 4446 8899 0000
'2446 4446 8899 0000'
>>> x
12.345
>>> x = input("Card number ")
Card number 2446 4446 8899 0000
>>> x
'2446 4446 8899 0000'
>>> len (x)
19
>>> x = int(x)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x = int(x)
ValueError: invalid literal for int() with base 10: '2446 4446 8899 0000'
>>> x = input("Card number ")
Card number 2446444688990000
>>> x
'2446444688990000'
>>> x = int(x)
>>> x % 10_000
0
>>> x = 123
>>> x // 100 + x % 10 + x //10 % 10
6
>>> a = 10
>>> b = 10
>>> c = 10
>>> p = a + b + c
>>> p
30
>>> a = 20
>>> b = 23
>>> c = 46
>>> p = (a + b + c) / 2
>>> p
44.5
>>> area = p * (p - a) * (p - b) * (p - c) ** 0.5
>>> area
(1.757887349751476e-12+28708.479064745618j)
>>> 