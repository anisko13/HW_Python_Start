text_1, text_2 = input('Your first word '), input('Your second word ')

text_1_set = set(text_1)
print(text_1_set)

text_2_set = set(text_2)
print(text_2_set)

print(text_1_set.intersection(text_2_set))


print(
    set(input('first text '))
        .intersection(set(input('second text ')))
)
