PI = 3.14159


def get_result(radius):
    return f'diameter is {radius * 2}, circumference is {radius * 2 * PI}, area is {radius * radius * PI}'


if __name__ == '__main__':
    result = get_result(
        int(input('Give me the radius ')),
    )
    print(result)
