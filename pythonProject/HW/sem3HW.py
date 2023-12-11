"""
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

Найдите количество и выведите его."""

# list_1 = [1, 2, 3, 3, 4, 5]
# k = 3
# count = 0
# for i in list_1:
#     if k == i:
#         count += 1
# print(count)

"""
Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

"""

# list_1 = [1, 2, 3, 4, 7]
# k = 6
#
# closest = list_1[0]
# dif = abs(k - list_1[0])
# for i in list_1:
#     current_dif = abs(k - i)
#     if current_dif < dif:
#         dif = current_dif
#         closest = i
# print(closest)


"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример:
k = 'ноутбук'
# 12
"""

eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in eng:
    summa = 0
    for letter in word:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa += key
    print(f'стоимость введенного английского слова = {summa}')
else:
    if word[0].lower() in rus:
        summa = 0
        for letter in word:

            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f'стоимость введенного русского слова = {summa}')