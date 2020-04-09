class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+self.pop())

    def sub(self):
        self.append(self.pop()-self.pop())
        # операция вычитания

    def mul(self):
        self.append(self.pop()*self.pop())
        # операция умножения

    def div(self):
        self.append(self.pop()//self.pop())
        # операция целочисленного деления


x = ExtendedStack([1,2,3,6.7])
x.div()
print(x)