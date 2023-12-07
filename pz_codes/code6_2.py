# Вариант 20
# 2. Дан целочисленный список размера N. Найти максимальное количество его одинаковых элементов.
def find_max_repeats(lst):
    repeats = {}
    for i in range(len(lst)):
        if lst[i] not in repeats:
            repeats[lst[i]] = 1
        else:
            repeats[lst[i]] += 1
    max_repeats = max(repeats.values())
    return f'Максимальное количество повторений элементов в списке: {max_repeats}'


string = input('Введите целочисленные элементы списка через пробел: ')
lst = []
for x in string.split(' '):
    lst.append(int(x))
print(find_max_repeats(lst))
