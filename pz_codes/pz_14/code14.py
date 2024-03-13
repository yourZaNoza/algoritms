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
    print(matches)
print(f'Количество фамилий в файле: {c}')

new = open(new_writer.txt, 'w')
