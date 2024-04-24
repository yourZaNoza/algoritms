class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1


note1 = Note("Task1")
note2 = Note("Task2")

print(note1.__dict__) #аттрибуты
print(dir(note1)) #все, что доступно переменной note1
print(note1.text)
print()

print(note2.__dict__) #аттрибуты
print(dir(note2)) #все, что доступно переменной note1
print(note2.text)
print()

note1.upcount()
print(note1.count)
note1.upcount()
print(note1.count)

print(note1.upcount) # bound - метод является привязанным для экземпляра note1
print(Note.upcount) # function - с точки зрения класса Note, upcount является обычной функцией


