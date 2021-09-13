a, b, c = [float(x) for x in input('Enter 3 numbers... ').split(' ')]  # [1, 2, 3]
if a > b > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
