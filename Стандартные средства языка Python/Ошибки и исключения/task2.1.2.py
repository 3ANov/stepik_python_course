import sys
sys.stdin = open("input.txt", "r")
n = int(input())

parents = {}

for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

print(parents)

#Ответ - m,e,g,f

q = int(input())
queue = []
for i in range(q):
    queue.append(input())
print(queue)

def is_parent(child, parent):
    if child == parent:
        return True

    for p in parents[child]:
        if is_parent(p, parent):
            return True

    return False




