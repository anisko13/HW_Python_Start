def element_concat_list(number1: int, number2: int, text: str) -> str:
    return text + str(number1 + number2)


if __name__ == '__main__':
    result = element_concat_list(2, 3, 'sum is ')
    print(result)
    