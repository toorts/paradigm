import random

numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)


def sort_list_declarative(numbers: list[int]) -> list[int]:
    return sorted(numbers)[::-1]


print(sort_list_declarative(numbers))