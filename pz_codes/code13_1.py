import random

N = int(input('Введите количество строк матрицы: '))
M = int(input('Введите количество столбцов матрицы: '))
A = [[random.randint(-10, 10) for x in range(M)] for z in range(N)]

row_sum = [sum(row) for row in A[:2]]
print(f'Матрица: {A}')
print(f'Сумма чисел построчно: {row_sum}')
print(f'Сумма всех чисел в первых двух строках: {row_sum[0] + row_sum[1]}')
