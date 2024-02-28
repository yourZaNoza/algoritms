# Вариант 20
# 1. Дано целое положительное число. Вывести символы, изображающие цифры этого числа (в порядке слева направо).
def print_digits_as_string(number):
  digits = []
  while number > 0:
    current_digit = number % 10
    digits.append(current_digit)
    number //= 10
  digits.reverse()
  return f'Цифры этого числа: {digits}'


number = int(input('Введите целое положительное число: '))
print(print_digits_as_string(number))
