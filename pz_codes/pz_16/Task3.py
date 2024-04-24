# Создать класс Person с одним атрибутом класса (count), с конструктором __init__ и одним статическим методом
# Увеличение количества созданных экземпляров обеспечить в конструкторе __init__
# Статический метод total_people должен обеспечить построение и вывод фразы о количестве созданных экземпляров

class Person:

    count = 0

    def __init__(self, name=""):
        self.name = name
        Person.count += 1

    @staticmethod
    def total_people():
        print(f'Количество созданных экземпляров = {Person.count}')


p1 = Person("Зоя")
p2 = Person("Фая")
p3 = Person()

print(p1.name)
print(p2.name)
Person.total_people()
