# Вариант 20.
# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных
# и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Числа кратные трем:
# Количество чисел кратных трем:


ls = ['-99 6 12 -36 20 45 100 -15 28 -4 2746 -25 76 -95']

f3 = open('data_3.txt', 'w')
f3.writelines(ls)
f3.close()

f4 = open('data_4.txt', 'w')
# f4.write('Исходные данные: ')
# f4.write('\n')
# f4.writelines(ls)
print('Исходные данные: ', ls, file=f4)
f4.close()

f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f3 = open('data_3.txt')
mn, t, c = 0, 0, 0
lst = []
for i in range(len(k)):
    if k[i] % 3 == 0:
        c += 1
        lst.append(k[i])
    mn = mn if mn < k[i] else k[i]
    if k[i] > 0:
        t += 1

f4 = open('data_4.txt', 'a')
print('Количество элементов: ', len(k), file=f4)
print('Минимальный элемент: ', mn, file=f4)
print('Числа кратные трём: ', lst, file=f4)
print('Количество чисел кратных трём: ', c, file=f4)
f4.close()
