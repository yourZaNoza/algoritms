# Вариант 20.
# 2. Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string.
# Строка 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'.
from string import ascii_lowercase

string_new = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
str_n = {i for i in string_new if i in ascii_lowercase}
print('Найдены все уникальные прописные буквы:')
print(str_n)
