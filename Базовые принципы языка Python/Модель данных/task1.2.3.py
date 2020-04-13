objects = [1, 2, 1, 2, 3, 1]
p = {}
for i in objects:
    p[id(i)] = id(i)
print(len(p))

