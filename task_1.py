https://github.com/YaDmitryE/py_lesson_5

# Вводим целое число
number = int(input("Введите целое число: "))

# Проверяем, является ли число четным и не является ли нулем
if number % 2 == 0 and number != 0:
    print("отрицательное четное число" if number < 0 else "положительное четное число")
elif number == 0:
    print("нулевое число")
else:
    print("число не является четным")
