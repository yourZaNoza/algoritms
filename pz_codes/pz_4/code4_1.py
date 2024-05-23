# Вариант 20.
# 1. Дано вещественное число Х и целое число N (> 0).
# Найти значение выражения 1 - Х**2/(2!) + Х*/(4!) - ... + (-1)**N-X**2*N/((2*N)!) (N != 12 ...).
# Полученное число является приближенным значением функции cos в точке Х.
import math

print('Считаем значение функции cos x')
x = int(input('Введите целое число: '))
cos = 0
for n in range(0, 13):
    cos += ((-1)**n) * (x**(2*n))/math.factorial(2*n)
print(f'Приблизительное значение функции = {cos}')