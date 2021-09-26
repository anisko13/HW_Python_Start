k = 1
x = 0
for k in range(1, 1000000):
    x = x+4 * ((-1) ** (k+1)) / (2*k-1)
for j in range(2, 13):
    print(round(x, j))
