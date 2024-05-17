# Для задачи из блока 1 создать две функции, save_def u load_def, которые позволяют сохранять информацию
# из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации
# и десериализации объектов Python B бинарном формате.

import pickle


class Counter:

    def __init__(self, count):
        self.count = count

    def upcount(self, plus):
        self.count += plus
        print(f'{self.count-plus} + {plus} = {self.count}')

    def discount(self, minus):
        self.count -= minus
        print(f'{self.count+minus} - {minus} = {self.count}')

    def save_def(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def load_def(self, filename):
        with open(filename, "rb") as file:
            loaded_object = pickle.load(file)
            self.count = loaded_object.count

# Пример использования
# Создаем объекты класса
c1 = Counter(5)
c2 = Counter(6)
c3 = Counter(7)

# Сохраняем объекты в файлы
c1.save_def("c1.pickle")
c2.save_def("c2.pickle")
c3.save_def("c3.pickle")

# Загружаем объекты из файлов
loaded_object1 = Counter("")
loaded_object1.load_def("c1.pickle")
print(f"Загруженный объект 1: {loaded_object1.count}")

loaded_object2 = Counter("")
loaded_object2.load_def("c2.pickle")
print(f"Загруженный объект 2: {loaded_object2.count}")

loaded_object3 = Counter("")
loaded_object3.load_def("c3.pickle")
print(f"Загруженный объект 3: {loaded_object3.count}")
