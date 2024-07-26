# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# data_inicio = datetime(2020, 12, 20)
valor_emprestimo = 1_000_000
data_inicio = datetime.strptime('20/12/2020', '%d/%m/%Y')
delta_anos = relativedelta(years=5)
data_final = data_inicio + delta_anos


data_parcelas = []
data_parcela = data_inicio
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
print(numero_parcelas)

valor_parcela = valor_emprestimo / numero_parcelas
print(valor_parcela)

for data in data_parcelas:
    print(f'{data.strftime('%d/%m/%Y')} {valor_parcela:,.2f}')


print()
print(
    f'Você pegou {valor_emprestimo:,.2f} para pagar',
    f'em {delta_anos.years} anos ({numero_parcelas} meses)',
    f'em parcelas de {valor_parcela:,.2f}'
)