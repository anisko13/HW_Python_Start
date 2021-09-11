def get_last_4_numbers(card: str) -> str:
    card.replace(' ', '')
    return card[-4:]


if __name__ == '__main__':
    result = get_last_4_numbers(
        input('Give me card number '),  # 0000 0000 0000 0000
    )
    print(f'Last 4 numbers are {result}')
