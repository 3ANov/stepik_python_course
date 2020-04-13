namespaces = {
    'global': {'parent': None, 'vars': []},
}


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
    namespaces[namespace] = {'parent': parent, 'vars': []}


def add(namespace, var):
    dict = namespaces[namespace]
    dict['vars'].append(var)


def get(namespace, var):
    if namespace is None:
        print(None)
        return
    if var in namespaces[namespace]['vars']:
        print(namespace)
        return
    get(namespaces[namespace]['parent'], var)





#translate()

add('global', 'a')
create('foo', 'global')
print(namespaces)
# print(reverse_dict)
add('foo', 'b')
print(namespaces)
get('foo', 'a')
print(namespaces)
get('foo', 'c')
print(namespaces)
create('bar', 'foo')
add('bar', 'a')
print(namespaces)
get('bar', 'a')
print(namespaces)
get('bar', 'b')







