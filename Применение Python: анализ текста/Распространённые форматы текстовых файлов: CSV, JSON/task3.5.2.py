import json
with open("input.json") as read_file:
    js = json.load(read_file)
child = dict()
parents = dict()


def f(i, k, child, parents):
    for j in child:
        if k in child[j]:
            parents[i].append(j)
            f(i, j, child, parents)


for i in js:
    child[i['name']] = i['parents']

for i in child:
    parents[i] = []

for i in parents:
    f(i, i, child, parents)

for i in sorted(parents):
    print(i, ':', len(set(parents[i])) + 1)