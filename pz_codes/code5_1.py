# Вариант 20
# 1. Составить функцию, которая напечатает сорок любых символов.
import random


def print_forty_symbols(symbols):
  for symbol in symbols:
    print(symbol, end="_")


symbols = [chr(random.randint(32, 126)) for _ in range(40)]
print_forty_symbols(symbols)
