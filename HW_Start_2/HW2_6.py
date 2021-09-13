a, b, c = [float(x) for x in input('Enter 3 sides... ').split(' ')]
p = (a + b + c) / 2
result = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(result)
