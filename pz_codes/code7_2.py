# Вариант 20
# 2. Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими).
# Преобразовать каждое слово в строке, заменив в нем все последующие вхождения его первой буквы на символ «.» (точка).
# Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У.». Количество пробелов между словами не изменять.

def count_spaces(string):
    counts = []
    current_count = 0

    for i in range(len(string)):
        c = string[i]
        if c == ' ':
            current_count += 1
        else:
            counts.append(current_count) if current_count != 0 else...
            current_count = 0

    if len(counts) < len(string.split()):
        counts.insert(0, 0)

    return counts


def new_text(txt):
    letters = txt.split()
    spaces = count_spaces(txt)

    for letter in letters:
        if not letter.isupper():
            return 'Кажется, введённый текст не написан заглавными буквами!'

    result = []
    for i, word in enumerate(letters):
        first_letter = word[0]
        new_word = " " * spaces[i] + first_letter + word[1:].replace(first_letter, '.')
        result.append(new_word)
    return ''.join(result)


text = input("Введите текст заглавными буквами: ")
print(new_text(text))
