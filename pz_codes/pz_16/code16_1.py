# 20. Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для инкремента и декремента значения.

class Counter:

    def __init__(self, count):
        self.count = count

    def upcount(self, plus):
        self.count += plus
        print(f'{self.count-plus} + {plus} = {self.count}')

    def discount(self, minus):
        self.count -= minus
        print(f'{self.count+minus} - {minus} = {self.count}')


c1 = Counter(5)
c1.upcount(2)
c1.discount(3)
c1.upcount(-8)

