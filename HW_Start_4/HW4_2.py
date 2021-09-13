def check_palindrome (number):
    str(number)
    [float(x) for x in str(number)]
    number_list = [float(x) for x in str(number)]  # 100 001
    # if number_list[0:3] == number_list[::-1][0: 3]:
    if [number_list[0], number_list[1], number_list[2]] == [number_list[5], number_list[4], number_list[3]]:
        print('You have a palindrome')
    else:
        print('You have not a palindrome')


if __name__ == '__main__':
    check_palindrome (
        int(input('Give me six number\'s '))
    )