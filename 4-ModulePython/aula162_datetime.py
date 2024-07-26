# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')

# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
# from pytz import timezone

date = datetime.now()
print(date.timestamp()) # isso está na base de dados
print(datetime.fromtimestamp(1715725413.553343))
# data_str = '2024-05-14 19:04:30'
# # data_str = '14-05-2024 19:04:30'
# data_str = '14/05/2024'
# data_str_frmt = '%d/%m/%Y'

# date = datetime.strptime(data_str, data_str_frmt)
