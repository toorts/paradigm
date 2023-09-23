import random


def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # Найдено вхождение, но это может быть не первое
            # Поэтому мы проверяем элементы слева от mid
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    lst = [random.randint(0, 9) for _ in range(10)]
    lst.sort()
    print(lst)

    num = random.randint(0, 9)

    result = binary_search(lst, num)

    if result != -1:
        print(f"Элемент {num} найден по индексу {result}.")
    else:
        print(f"Элемент {num} не найден в массиве.")
