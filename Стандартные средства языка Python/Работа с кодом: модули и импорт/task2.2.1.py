from datetime import datetime
from datetime import timedelta

str_date = input()
days = timedelta(days=int(input()))

date = datetime.strptime(str_date, '%Y %m %d').date()+days

print(date.year,date.month,date.day )