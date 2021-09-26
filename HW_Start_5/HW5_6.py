import random

list1 = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
print(list1 + [x * 2 for x in list1])  # [x for x in list] : [13, 8, 8, 8] => [26, 16, 16, 16]
