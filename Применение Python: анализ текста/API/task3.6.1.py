import requests


with open('input.txt') as inp:
    for num in inp:
        print(num)
        url = "http://numbersapi.com/"+num.rstrip()+"/math?json=true"
        print(url)
        res = requests.get(url)
        print(res.json())

