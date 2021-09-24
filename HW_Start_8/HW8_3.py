text = input('enter text ')
result = {}

for letter in text:  # aad => {a = 1}, {a = 2}, {a=2, d=1}
    if letter == ' ':
        continue
    if letter not in result:
        result[letter] = 1
    else:
        result[letter] += 1
print(result)
