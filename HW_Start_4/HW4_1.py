def check_happy_ticket(number):
    str(number)  # int 3443 => str 3443
    [float(x) for x in str(number)]  # str 3443 => [3.0, 4.0, 4.0, 3.0]
    number_list = [float(x) for x in str(number)]  # 3443 => [3, 4, 4, 3]
    if number_list[0] + number_list[1] == number_list[2] + number_list[3]:
        print('You have a happy ticket')
    else:
        print('You have not a happy ticket')


if __name__ == '__main__':
    check_happy_ticket(
        int(input('Give me four number\'s ticket '))
    )
