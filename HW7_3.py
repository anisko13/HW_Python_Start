text = input('Enter name ')
counter = 0
for char in text:
    counter += ord(char)
    print(char, ord(char))
print(counter)
