# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
# data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')

fmt = '%d/%m/%Y'
fmt_1 = '%d/%m/%Y %H:%M'
fmt_2 = '%d/%m/%Y %H:%M:%S'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime(fmt_1))
print(data.strftime(fmt_2))