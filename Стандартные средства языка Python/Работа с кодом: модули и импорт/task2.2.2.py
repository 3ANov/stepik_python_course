import requests
from simplecrypt import encrypt, decrypt



encrypted = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
passwords_list = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').text.split()
for password in passwords_list:
    try:
        plaintext = decrypt(password, encrypted)
        print(plaintext)
    except:
        continue


