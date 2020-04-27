import requests
import re

start = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
end = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
link_template = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

res = requests.get(start)
print(res.text)


def search_link(res):
    for link in re.findall(link_template, res.text):
        res = requests.get(link)
        print(res.text)
        if res.text.find(end) != -1:
            return 'Yes'
    return 'No'


print(search_link(res))
