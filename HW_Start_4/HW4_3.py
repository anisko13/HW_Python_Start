x, y = [float(x) for x in input().split()]  # '1 2' => ['1', '2'] => [1.0, 2.0]
print(x * x + y * y < 16)