# Вариант 20.
# 2. Даны два числа. Вывести вначале большее, а затем меньшее из них

n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
if n1 > n2:
    print(f'Число {n1} больше числа {n2}')
else:
    print(f'Число {n2} больше числа {n1}')