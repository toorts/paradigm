import random

numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)


def sort_list_imperative(numbers: list[int]):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


sort_list_imperative(numbers)
print(numbers)