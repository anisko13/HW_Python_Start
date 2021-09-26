list1 = []

list2 = []
for index in range(1, 17):
    list2.append(index)
    if index % 4 == 0:
        list1.append(list2)
        list2 = []


list1 = []

counter = 1
for _ in range(4):
    list2 = []
    for _ in range(4):
        list2.append(counter)
        counter += 1
    list1.append(list2)
print(*list1, sep='\n')

some_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print(sum([sum(x) for x in some_matrix]))