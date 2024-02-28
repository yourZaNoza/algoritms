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
A = [[random.randint(-10, 10) for x in range(M)] for z in range(N)]
print(A)


find_min_max(A)
