# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# РЕШЕНИЕ:

# number = int(input('Введите размер списка: '))
# list = []
# sum = 0
# for i in range(number):
#     list_number = int(input(f'Введите число: {i+1} '))
#     list.append(list_number)
#     if i % 2 != 0:
#         sum += list[i]
# print(list)
# print(f'Сумма нечетных чисел равна: {sum}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# РЕШЕНИЕ:
# 1. вариант решения
# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)
# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)
# lst = list(map(int, input("Введите числа через пробел: \n").split()))
# mult_lst(lst)
# 2. вариант решения
# from random import randint
# number = int(input('Введите размер списка '))
# list = []
# list2 = []
# for i in range(number):
#     list.append(randint(0, 9))
# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# РЕШЕНИЕ:

# from random import uniform
# def get_real_num (n, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(n)]
# def find_diff(my_num):
#     num = [round(x - int(x), 2) for x in (my_num)]
#     return max(num) - min(num)
# n = 5
# frst = 1
# last = 10
# my_num = get_real_num(n, frst, last)
# print (my_num)
# print(find_diff(my_num))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
# РЕШЕНИЕ:

# a = ''
# b = int(input('Введите целое число: '))
# while b != 0:
#     a = str(b%2) + a
#     b //=2
# print(a)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# РЕШЕНИЕ:
# n = int(input('Введите целове число: '))
# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2
# list = [0]
# userNumber = int(input('Введите целове число: '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)