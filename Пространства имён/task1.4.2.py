namespaces = {}
reverse_dict = {}


def translate():
    n = int(input())
    for i in range(n):
        cmd, namesp, arg = input().split()
        if cmd == 'create':
            create(namesp, arg)
        if cmd == 'add':
            add(namesp, arg)
        if cmd == 'get':
            get(namesp, arg)


def create(namespace, parent):
    if namespaces.get(parent) is None:
        namespaces[parent] = [namespace]
    else:
        namespaces[parent] += [namespace]


def add(namespace, var):
    if namespaces.get(namespace) is None:
        create(var, namespace)
    else:
        namespaces[namespace] += var


def get(namespace, var):
    for space in namespaces:
        for child in namespaces[space]:
            reverse_dict[child] = space
    parent = reverse_dict.get(var)
    if parent is not None:
        print(parent)
        return
    if parent != namespace:
        print(reverse_dict.get(parent))
    else:
        print(None)




#translate()

add('global', 'a')
# print(namespaces)
# print(reverse_dict)
create('foo', 'global')
# print(namespaces)
# print(reverse_dict)
add('foo', 'b')
# print(namespaces)
# print(reverse_dict)
get('foo', 'a')
# print(namespaces)
# print(reverse_dict)
get('foo', 'c')
# print(namespaces)
# print(reverse_dict)
create('bar', 'foo')
create('car', 'bar')
add('bar', 'a')

get('car', 'a')

get('bar', 'b')





