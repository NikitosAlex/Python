# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def InputNumbers(inputText):
    global number
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")


# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def InputNumbers(inputText):
    global number
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх
# знаков после точки.

n = int(input("Введите размер списка: "))
a = []
sumElements = 0

for i in range(n):
    new_element = ((1 + 1 / (i + 1)) ** (i + 1))
    a.append(new_element)
print(f'Ваш список: {a}')

sumElements = round(sum(a), 3)
print(f'Сумма Вашего списка: {sumElements}')

# Задание 4  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

import random


def multyply(a, b):
    return list[a] * list[b]


n = int(input("Введите число "))
list = []
for i in range(n):
    list.append(random.randint(-n, n))
print("Получившийся список ", list)
while True:
    a = int(input("Введите первую позицию "))
    if a > 0 and a <= n:
        break
while True:
    b = int(input("Введите вторую позицию "))
    if 0 < b <= n:
        break
print("Произведение элементов на указанных позициях ", multyply(a - 1, b - 1))

# Задание 5 Реализуйте алгоритм перемешивания списка.

import random


def get_list():
    list = []
    for i in range(1, 100):
        list.append(i)
    return list


def rnd_shuffle(list):
    return random.shuffle(list)


list = get_list()
print(f'Список до перемешивания: {list}')
rnd_shuffle(list)
print(f'Перемешанный список: {list}')

# Задание 6 Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
# вхождений одной строки в другой.

text1 = str(input('Введите текст: '))
text2 = str(input('Введите искомый элемент: '))

print(text1.count(text2))
