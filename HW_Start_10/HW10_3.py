def draw_rectangle(weight: int, height: int) -> None:

    for index in range(height):
        if index == 0 or index == height - 1:
            print(f'{"*" * weight} ')
            continue
        print(f'*{" " * (weight-2)}*')

    for i in range(height):
        if not i or i == height - 1:
            print(' *' * weight, end='')
            print()
        else:
            print('*' + ' ' * (height - 2) + '*')

if __name__ == '__main__':
    draw_rectangle(weight=5, height=10)