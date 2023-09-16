import math
import random


def mean(arr: list[int]) -> float:
    """Функия для вычисления среднего значения массива"""
    return sum(arr) / len(arr)


def pearson_correlation(arr1: list[int], arr2: list[int]) -> float:
    # Вычисляем средние значения для обоих массивов
    mean1 = mean(arr1)
    mean2 = mean(arr2)

    # Вычисляем числитель и знаменатель для формулы корреляции Пирсона
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(arr1, arr2))
    denominator1 = sum((x - mean1) ** 2 for x in arr1)
    denominator2 = sum((y - mean2) ** 2 for y in arr2)

    # Вычисляем корреляцию Пирсона
    correlation = numerator / math.sqrt(denominator1 * denominator2)

    return correlation


if __name__ == '__main__':

    array1 = [random.randint(0, 9) for _ in range(10)]
    array2 = [random.randint(0, 9) for _ in range(10)]
    print(f'Массив 1: {array1}')
    print(f'Массив 2: {array2}')

    result = pearson_correlation(array1, array2)
    print(f'Корреляция Пирсона между массивама: {result}')
