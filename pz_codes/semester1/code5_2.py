# Вариант 20
# 2. Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать данный прямоугольник,
# если от него каждый раз отрезать квадрат наибольшей площади.

def rectangle(a, b):
    count = 0
    cf = a/b if a>b else b/a
    if a > b:
        v = a/cf
        while v > 1:
            v /= cf
            count += 1
    else:
        v = b/cf
        while v > 1:
            v /= cf
            count += 1

    return f'В прямоугольнике размером {a}*{b}, {count} квадратов'


print(rectangle(13, 8))