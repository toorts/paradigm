import random


def sort_list_imperative(arr: list[int]) -> list[int]:
    size = len(arr)

    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':

    numbers = [random.randint(-10, 10) for _ in range(10)]
    print(numbers)
    print(sort_list_imperative(numbers))
