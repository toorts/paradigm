n = int(input("Введите число n: "))

if n <= 0:
    print("Число n должно быть положительным.")
else:
    print("Таблица умножения:")

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result = i * j
            print(f"{i} * {j} = {result}")
