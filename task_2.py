# https://github.com/YaDmitryE/py_lesson_5

# Введите слово с помощью input()
word = input("Введите слово из маленьких латинских букв: ")

# Создайте переменные для подсчета количества гласных и согласных букв
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonants = 0

# Переберите буквы в слове и определите, является ли она гласной или согласной
for letter in word:
    if letter in vowels:
        vowels[letter] += 1
    elif letter.isalpha():
        consonants += 1

# Проверьте, есть ли все гласные буквы в слове
if all(vowels.values()):
    print(f"Гласные: {', '.join([f'{k}: {v}' for k, v in vowels.items()])}")
    print(f"Согласные: {consonants}")
else:
    print(False)
