from xml.etree import ElementTree as et


tree = et.parse('task.xml')
root = tree.getroot()

# функция(верхний кубик, уровень):
#     повышаем уровень на 1
#     добавляем в словарь цвет кубика
#     обходим детей кубика:
#         и уже для каждого из них вызываем нашу функцию
answer = {'red': 0, 'green': 0, 'blue': 0}


def leveling(cube, level):
    answer[cube.attrib['color']] += level
    level += 1
    for child in cube:
        leveling(child, level)


leveling(root, 1)
print(str(answer['red'])+' '+str(answer['green'])+' '+str(answer['blue']))
