# 20. Создание базового класса "Работник" и его наследование для создания классов "Менеджер" и "Инженер".
# В классе "Работник" будут общие методы, такие как "работать" и "получать зарплату", а классы-наследники будут
# иметь свои уникальные методы и свойства, такие как "управлять командой" и "проектировать системы".

class Worker:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def work(self):
        print(f"{self.name} {self.surname} выполняет свою работу.")

    def get_salary(self):
        print(f"{self.name} {self.surname} получает зарплату.")


class Manager(Worker):

    def __init__(self, name, surname, department):
        super().__init__(name, surname)
        self.department = department

    def commanding(self):
        print(f"{self.name} {self.surname} руководит командой в отделе {self.department}.")


class Engineer(Worker):


    def __init__(self, name, surname, specialization):
        super().__init__(name, surname)
        self.specialization = specialization

    def system_projecting(self):
        print(f"{self.name} {self.surname} проектирует системы в области {self.specialization}.")


worker1 = Worker("Иван", "Петров")
worker1.work()
worker1.get_salary()

manager1 = Manager("Василий", "Сидоров", "Маркетинг")
manager1.work()
manager1.get_salary()
manager1.commanding()

engineer1 = Engineer("Ольга", "Кузнецова", "Программное обеспечение")
engineer1.work()
engineer1.get_salary()
engineer1.system_projecting()
