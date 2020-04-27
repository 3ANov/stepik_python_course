# put your python code here
import requests
import re

start = 'http://pastebin.com/raw/7543p0ns'
#href=[\'|\"]((\w*\:\/\/)?)(\b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b)
link_template = r'<a.*href=[\'|\"]((\w*\:\/\/)?)(\b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b)'
res = requests.get(start)
domain_name = []

#print(re.findall(link_template, res.text))
result = set()
for group in re.findall(link_template, res.text):
    #print(group[2])
    result.add(group[2])

result = list(result)
result.sort()
for line in result:
    print(line)