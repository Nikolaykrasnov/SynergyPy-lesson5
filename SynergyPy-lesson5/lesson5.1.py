namber = int (input("Введите число:"))
if namber == 0:
    print("Нулевое число")
elif namber > 0 and namber % 2 == 0:
    print("Положительное четное число")
elif namber > 0 and namber % 2 != 0:
    print("Положительное нечетное число")
elif namber < 0 and namber % 2 == 0:
    print("Отрицательное четное число")
elif namber < 0 and namber % 2 != 0:
    print("Отрицательное нечетное число")