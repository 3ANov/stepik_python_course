class Buffer:
    def __init__(self):
        self.space = []
        # конструктор без аргументов

    def add(self, *a):
        for i in a:
            self.space.append(i)
            if len(self.space) == 5:
                print(sum(self.space))
                self.space.clear()
        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.space
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)
print(buf.get_current_part())
buf.add(7, 8, 9, 10)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part())