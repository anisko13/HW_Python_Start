set_1 = {elem * 3 for elem in range(1, 100)}  # [item for elem in list]
set_2 = {elem * 5 for elem in range(1, 100)}

print(set_1.intersection(set_2))

list_1_alternative = []
for elem in range(1, 100):
    list_1_alternative.append(elem * 3)
