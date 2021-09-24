def find_element(arr: list, target: int) -> int:
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

if __name__ == '__main__':
    print(find_element([1,2,3,4,5], 5))
