import random


def find_min_max(A):
    mn_num = 0
    mx_num = 0

    for row in A:
        for num in row:
            mn_num = min(mn_num, num)
            mx_num = max(mx_num, num)

    print("Минимальное число: ", mn_num)
    print("Максимальное число: ", mx_num)


N = 3
M = 3
A = [[0]*M for z in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(-10, 10)
for x in range(len(A)):
    for y in range(len(A[x])):
        print(A[x][y], end=' ')
    print()


find_min_max(A)
