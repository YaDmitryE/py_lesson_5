# https://github.com/YaDmitryE/py_lesson_5

# Вводим сумму инвестиций X
X = int(input("Введите минимальную сумму инвестиций X: "))

# Вводим суммы инвестиций Майкла и Ивана
A = int(input("Введите сумму инвестиций Майкла A: "))
B = int(input("Введите сумму инвестиций Ивана B: "))

# Проверяем возможные варианты
if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)
