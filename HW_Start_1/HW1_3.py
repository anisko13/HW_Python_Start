def count_rectangle_area(length, width):
    return length * width


if __name__ == '__main__':
    result = count_rectangle_area(
        int(input('Give me the width ')),
        int(input('Give me the length '))
    )
    print(f'rectangle area is {result}')
