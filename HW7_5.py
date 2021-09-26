some_text = input('enter text')
memory = ''
for word in some_text.split():
    if len(word) > len(memory):
        memory = word
print(memory)
