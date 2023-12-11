"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""


"""lst = "a a a b c a a d c d d".split()
print(lst)
dct = {}
for item in lst:
    if item in dct:
        print(f"{item}_{dct[item]}", end=' ')
    else:
        print(item, end=' ')
    dct[item] = dct.get(item, 0) + 1 #функция get позволяет сделать дефолтное значение, даже если элемента еще не было
"""
"""
some_str = 'a a a b c a a d c d d'.split()
a = ''

for i in some_str:
    count = a.count(i)
    if a.count(i) == 0:
        a += i + ' '
    else:
        a += i + '_' + str(count) + ' '

print(a)
"""


"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
"""
"""
twister = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells""".lower().split()
print(len(set(twister)))
"""

"""
#не оптимальный код
text_str = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""
text_str = text_str.lower()  # переводим всю строку в нижний регистр
text_str = text_str.replace(".", "")  # удаляем из строки знаки препинания
text_str = text_str.split()  # разбиваем строку по разделителю
word_set = set()
# добавляем элементы строки в множество при этом удаляются одинаковые слова
for word in range(len(text_str)):
    word_set.add(text_str[word])
print(len(word_set))
"""

"""import re
s = ("She sells sea shells on the sea shore;The shells that "
     "she sells are sea shells I'm sure. So if she sells sea "
     "shells on the sea shore,I'm sure that the shells are sea shore shells")
delimiters = r"[;,:.\' ]+"
s = re.split(delimiters, s)
print(len(set(s)))"""

"""
Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
"""
# Ваня:
"""n = int(input())
max_number = 1000
while n != 0:
     n = int(input())
     if max_number > n:
         max_number = n
         print(max_number)"""


# #Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
#         print(n)

"""n = int(input())
max_number = n
while n!= 0
    if n > 0:
        n = int(input())
        if max_number > n:
            max_number = n
print(max_number)"""
# У Пети четыре(4) ошибки, а у Вани 2.

