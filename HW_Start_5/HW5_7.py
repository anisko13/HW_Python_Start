import random

list1 = []
for i in range(12):
    list1.append(random.randint(7500, 15000))

print(sum(list1) // len(list1))
