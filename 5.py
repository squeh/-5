nominali = [5000,2000,1000,500,200,100]

amount = int(input("Введите сумму: "))

if amount % 100 != 0 or amount <= 0:
    print("Сумма должна быть положительной и делиться на 100")
else:
    print("Банкомат выдаст: ")
    for nom in nominali:
        count = amount // nom
        amount = amount % nom
        if count > 0:
            print(nom, "руб. - ",count, "шт.")
