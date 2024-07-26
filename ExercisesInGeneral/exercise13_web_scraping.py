# Você foi contratado por uma empresa de consultoria meteorológica para 
# desenvolver um programa que faça raspagem de dados de previsão do tempo de um 
# site de meteorologia e os organize em um formato legível para análise posterior.
# O site que você irá raspar contém informações diárias de temperatura máxima e mínima,
# bem como as condições meteorológicas para os próximos 5 dias.

# Tarefas a serem realizadas:

# Escolha um site de previsão do tempo para realizar a raspagem de dados. 

# # Utilize uma biblioteca de raspagem de dados, como BeautifulSoup em Python, 
# para extrair as seguintes informações para cada dia:

# ---- Data
# ---- Temperatura máxima
# ---- Temperatura mínima
# ---- Condições meteorológicas (ensolarado, chuvoso, nublado, etc.)
# ---- Organize os dados extraídos em um formato estruturado, como um dicionário em Python.

# Escreva o código para realizar a raspagem de dados e armazená-los em uma estrutura de dados.

# Apresente os dados raspados de forma legível, por exemplo, imprimindo as informações na tela.

# Desafio adicional:

# Além de extrair os dados para os próximos 5 dias, implemente a funcionalidade 
# para extrair dados adicionais, como a umidade, velocidade do vento e probabilidade 
# de precipitação. 


import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/pt-BR/clima/10dias/l/dfb390d5d0537ed3c80f13693bce4fb5ab75fb5fa1ddd5c46fb61fc04264005d'
response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

part_climate = parsed_html.select('#WxuDailyCard-main-a43097e1-49d7-4df7-9d1a-334b29628263 > section > div.Card--content--1GQMr.DailyForecast--CardContent--2YlvT > div.DailyForecast--DisclosureList--nosQS')[0]
div_information = part_climate.select('div[data-testid="DetailsSummary"]')[0]

# for _ in div_information:
#     print(len(_))

print(len(div_information))
    

divs = div_information.select('#DaypartDetails--DayPartDetail--2XOOV Disclosure--themeList--1Dz21')
print(len(divs))
# print(divs)

# # for datail in div_information.select(''):
# #     print(datail.text)


