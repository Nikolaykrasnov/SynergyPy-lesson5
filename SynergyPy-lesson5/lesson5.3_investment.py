min_investment = int(input("Введите минимальную сумму инвестирования:"))
mike = int(input("Введите сумму денек Майкла:"))
ivan = int(input("Введите сумму денег Ивана:"))

if mike >= min_investment and ivan >= min_investment:
    print(2)
elif mike >= min_investment or ivan >= min_investment or mike + ivan >= min_investment:
    print(1)
else: 
    print(0)