# put your python code here
import requests
import re


start = input()
link_template = r'<a.*href=[\'|\"]((\w*\:\/\/)?)(\b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b)'
res = requests.get(start).text


result_set = set()
for group in re.findall(link_template, res):
    result_set.add(group[2])

result = list(result_set)
result.sort()
for line in result:
    print(line)