# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10)
delta = relativedelta(data_fim, data_inicio)
print(delta.years)
# print(data_fim + delta)
# print(data_fim > data_inicio)

# --------------- TESTE ----------------
# print('Digite sua data de nascimento abaixo:')
# year = input('Enter your year:')
# month = input('Enter your month: ')
# day = input('Enter your day: ')

# date_str = f'{day}/{month}/{year}'
# fmt = '%d/%m/%Y'
# date = datetime.strptime(date_str, fmt)
# date_now = datetime.now()

# date_formated = date_now - date
# print(date_formated)
# print(f'{date_formated.days / 365:.1f}')
# print(datetime.fromtimestamp(date_formated.total_seconds()))
# delta_sec = date_formated.timestamp()