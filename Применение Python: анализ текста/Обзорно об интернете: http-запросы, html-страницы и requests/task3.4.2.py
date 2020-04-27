import requests
import re
from urllib.parse import urlparse


with open('input.txt', 'r') as inp:
    for input_line in inp:
        print(input_line.rstrip().split('\''))



