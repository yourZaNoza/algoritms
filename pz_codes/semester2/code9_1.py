# Вариант 20
# Используя словарь посчитать количество уникальных слов в заданном предложении «Изучаем язык Питон».
# Вывести на экран каждую пару «ключ: значение»

sentence = "Изучаем язык язык Питон"
print(f'"{sentence}"')
words_dict = {}
words = sentence.split()

for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

for word, count in words_dict.items():
    print(f"{word}: {count}")
