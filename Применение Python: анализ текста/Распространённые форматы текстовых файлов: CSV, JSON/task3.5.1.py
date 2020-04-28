import csv
from datetime import datetime


with open('Crimes.csv') as f:
    reader = csv.reader(f)
    next(reader)
    answer = dict()
    for line in reader:
        #if datetime.strptime(line[2], '%m/%d/%Y %I:%M:%S %p').year == 2015:
        if '2015' in line[2]:
            if answer.get(line[5]) is None:
                answer[line[5]] = 0
            else:
                answer[line[5]] += 1


print(max(answer, key=answer.get))

