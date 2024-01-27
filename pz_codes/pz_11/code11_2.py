# -*- coding: utf-8 -*-
# Вариант 20.
# 2. Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.

mxl, a, b = 0, 0, 0
for i in open('text18-20.txt', encoding='utf-16'):
    print(i, end='')
    a += 1
    for j in i:
        b += 1
print(end='\n')
print(end='\n')
print('Количество строк: ', a, end='\n')
print('Количество символов в тексте : ', b, end='\n')

f1 = open('text18-20.txt', encoding='utf-16')
text = f1.read()
lines = text.splitlines()
max_line = max(lines, key=len)
f1.close()
f2 = open('text18-20-2.txt', 'w')
f2.writelines(max_line)
f2.close()
