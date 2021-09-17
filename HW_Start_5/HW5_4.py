w = int(input('Input the width: '))
h = int(input('Input the height: '))

for i in range(h):
    if not i or i == h-1:
        print('*'*w, end ='')
        print()
    else:
         print('*' + ' '*(w-2) + '*')