# Дано трехзначное число. Вывести число, полученное при
# перестановке цифр сотен и десятков исходного числа
# (например, 123 перейдет в 213).


number = input("Введите трёхзначное число: ")
try:
    a = int(number)
    if a < 100 or a > 999:
        print('Введено неверное число! Введите трёхзначное!')
    else:
        b = a % 100 % 10  # получение единиц
        c = a % 100  # получение десятков с единицами
        c = c - b  # получение десятка без единиц
        d = a % 1000  # получение сотен с десятками и единицами
        d = d - c - b  # получение сотен без десятков и единиц
        c = c // 10
        d = d // 100
        print(f'Ваше новое число: {c}{d}{b}')
except ValueError:
    try:
        float(number)
        print('Введено неверное число! Введите трёхзначное целое!')
    except:
        print('Введено не число!')


#  total = c * 100 + d * 10 + b
#  print(f'Ваше новое число: {total}')
#  print('Ваше новое число:', total)
