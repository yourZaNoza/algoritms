import random

N = int(input('Введите количество строк матрицы: '))
M = int(input('Введите количество столбцов матрицы: '))
A = [[0]*M for z in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(-10, 10)
for x in range(len(A)):
    for y in range(len(A[x])):
        print(A[x][y], end=' ')
    print()

row_sum = [sum(row) for row in A[:2]]
print(f'Сумма чисел построчно: {row_sum}')
print(f'Сумма всех чисел в первых двух строках: {row_sum[0] + row_sum[1]}')
