# Вариант 20.
# Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество фамилий.
# Создать новый файл, в котором выполнить замену слова "роман" на слово "произведение".

import re

file1 = open('writer.txt', 'r')
file1.readlines()
# f1 = re.findall(r'\bписатель\b', file1)
file1.close

print()

text = "My function(x, y) takes two arguments. I call it like this: my_function(a, b)."

# Use the 're.findall' function to find all matches in the text
matches = re.findall(r'\b\w+\b\s+(?=\()', text, re.IGNORECASE)

# Print the list of matches
print(matches)