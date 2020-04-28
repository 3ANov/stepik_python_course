from operator import itemgetter

import requests
import json

client_id = ''
client_secret = ''

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
answer = []

with open('input.txt') as inp:
    for artist in inp:
        artist = artist.rstrip()
        r = requests.get("https://api.artsy.net/api/artists/"+artist, headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        #answer[j['sortable_name']] = j['birthday']

        answer.append({'name': j['sortable_name'], 'birthday': j['birthday']})
        #print(j['name'], j['birthday'])
    #print(answer)

    sr = sorted(answer, key=itemgetter("birthday", 'name'))
    for line in sr:
        print(line['name'])