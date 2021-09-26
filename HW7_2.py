text = input('Enter name ')
for char in text:
    if char.isdigit():
        print(f'name has digit - {char}')
for word in text.split():
    if word[0].isupper():
        print('First char is OK')
    else:
        print('First char is not OK')
    for char in word[1:]:
        if char.islower():
            pass
        else:
            print('Else char is not OK')