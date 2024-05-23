# Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2-9.
# Для данной задачи был взят код из ПЗ №2 - code2.py
# Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа.
# (например, 123 перейдет в 213).
import tkinter as tk

def permute_digits():
  entered_num = entry.get()

  if not entered_num.isdigit() or len(entered_num) != 3:
    error_label.config(text="Ошибка: Ввведено не трёхзначное число!")
    return

  hundreds_digit = entered_num[0]
  tens_digit = entered_num[1]
  units_digit = entered_num[2]
  permuted_num = tens_digit + hundreds_digit + units_digit
  result_label.config(text=f"Переставленное число: {permuted_num}")


window = tk.Tk()
window.title("Перестановка цифр")

label = tk.Label(window, text="Введите трехзначное число:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Переставить", command=permute_digits)
button.pack()

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
