"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

"""
n = 11
m = 6
q_n = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
q_m = {3, 6, 9, 12, 15, 18}
c = q_n.intersection(q_m)
print(c)
d = list(c)
print(d)
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(d))
"""

"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0 = 0, a1 = 1,
ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
"""
"""
def fib(n):
    if n == 0 or n == 1:
        return 1
    #elif n == 1:
    #    return 1
    else:
        return fib(n - 1) + fib(n-2)
m = 7
print(fib(m))

list_1 = []
for i in range(1, 8):
    list_1.append(fib(i))
print(list_1)
"""

"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""
"""def min_to_max(grade_list, count, x):
    if count < 0:
        return grade_list
    count -= 1
    if grade_list[count] == x:
        grade_list[count] = min(grade_list)
    return min_to_max(grade_list, count, x)

list_1 = [1, 3, 3, 3, 4]
cnt = 5
print(min_to_max(list_1, cnt, max(list_1)))"""

"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 15
"""

"""
def is_prime_rec(n, max_div):
    if max_div == 1:
        return 'Yes'
    if n % max_div == 0:
        return 'No'
    return is_prime_rec(n, max_div - 1)


k = int(input("введите число: "))


print(is_prime_rec(k, round(k ** 0.5)))
"""

"""
def func_1(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag
print(func_1(9))
"""
"""
def func_2(num, flag=True, i=2):
    if i < num:
        if num % i == 0:
            flag = False
        return func_2(num, flag, i+1)
    return flag

print(func_2(7))
"""

"""
Задача №37. Решение в группах
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

def rev(n):
    if n > 0:
        num = int(input("Введите число: "))
        rev(n-1)
        print(num, end=' ')

rev(2)