from xml.etree import ElementTree as et

tree = et.parse('example.xml')
root = tree.getroot()

print(root.tag, root.attrib)
print(root[0][0].text)
for child in root:
    print(child.tag, child.attrib)

for el in root.iter('scores'):
    sum = 0
    for child in el:
        sum += float(child.text)
    print(sum)
tree.write('copy.xml')

greg = root[0]
module = next(greg.iter('module1'))
module.text = str(float(module.text) + 30)
print(module, module.text)
cert = greg[2]
cert.set('type', 'with')
tree.write('example_mod.xml')
