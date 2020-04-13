class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.volume = 0

    def can_add(self, v):
        return self.volume + v <= self.capacity
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.volume += v

x = MoneyBox(10)
print(x.volume)
x.add(5)
print(x.can_add(6))