# ИСХОДНЫЙ КОД ЗАДАЧИ

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# напишем функцию, которая заполняет, выводит список и подсчитывает сумму нечетных элементов списка
# def sum_num_lst(a,b):  # a и b - минимальное/максимальное значения длинны списка
#     lst = []
#     sum = 0
#     for i in range(a,b):
#         n = int(input("Укажите значение для элемента списка: "))
#         lst.append(n)
#     print(lst)
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             sum += lst[i]
#     return sum
#
# print(f"Cумма значений на нечетных позициях = {sum_num_lst(0,5)}")

# res = [(i, f(i) for i in range(len(lst))]


# Упрощаем код

# n = int(input())
# lst = [i for i in range(1, n+1)]

def f(lst,x):
    return lst[x]

lst = [2, 3, 5, 9, 3, 11, -6, 0]
lst = [(i,f(lst,i)) for i in range(len(lst)) if i % 2 != 0]
print(lst)