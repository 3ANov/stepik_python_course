namespaces = {}


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
    print(namespaces)


def add(namespace, var):
    if namespaces.get(namespace) is None:
        create(var, namespace)
    else:
        namespaces[namespace] += var


def get(namespace, var):
    if namespaces[namespace].count(var) != 0:
        print(namespace)
    else:
        return get(namespaces, namespace)




#translate()


translate()
create('foo', 'global')
create('foo2', 'global')
add('foo', 'a')
add('foo', 'b')




