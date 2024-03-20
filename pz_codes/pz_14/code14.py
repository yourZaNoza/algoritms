# -*- coding: utf-8 -*-
# Вариант 20.
# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество фамилий.
# Создать новый файл, в котором выполнить замену слова "роман" на слово "произведение".

import re
c = 0
for i in open('writer.txt', encoding='utf-8'):
    # print(i, end='')
    matches = re.findall(r'\S+(?=\s\w\.\w)', i)
    c += 1
    # print(matches)
print(f'Количество фамилий в файле: {c}')

# old = open('text18-20.txt', encoding='utf-16')
# text = old.read()
# lines = text.splitlines()
# rewrite = re.findall()
# old.close()
# new = open(new_writer.txt, 'w')
# new.writelines(max_line)
# new.close()

roman_endings = ['', 'а', 'ов']
prod_endings = ['ие', 'иев', 'ий', 'ия']

with open('writer.txt', 'r', encoding='utf-8') as f1:
    text = f1.read()
for re_ending in roman_endings:
    for pe_ending in prod_endings:
        pattern = r'\bроман(?=\b|' + re_ending + r')'
        replacement = 'произведен' + pe_ending
        text = re.sub(pattern, replacement, text)
with open('new_writer.txt', 'w', encoding='utf-8') as f2:
    f2.write(text)

