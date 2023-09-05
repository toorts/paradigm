import random


def sort_list_declarative(arr: list[int]) -> list[int]:
    return sorted(arr)[::-1]


if __name__ == '__main__':

    numbers = [random.randint(-10, 10) for _ in range(10)]
    print(numbers)
    print(sort_list_declarative(numbers))
