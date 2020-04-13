import sys
sys.stdin = open("input.txt", "r")
n = int(input())

parents = {}

for _ in range(n):
    a = input().split()
    parents[a[0]] = set([]) if len(a) == 1 else set(a[2:])

#print(parents)

#Ответ - m,e,g,f

q = int(input())


def is_parent(child, parent):
    if child == parent:
        return True

    try:
        for p in parents.get(child):
            if is_parent(p, parent):
                return True
    except:
        return False

    return False


#Ответ - m,e,g,f
queue = []
for _ in range(q):
    queue.append(input())

#print(queue)

for i in queue:
    for j in queue:
        if is_parent(i,j) and queue.index(i)>queue.index(j):
            print(i)
            break






