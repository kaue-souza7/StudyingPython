# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import requests
import re
from bs4 import BeautifulSoup

url = 'http://localhost:3330/'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# # print(parsed_html.title.text)

# top_jobs_heading = parsed_html.select('#intro > div > div > article > h2')[0]
# # print(top_jobs_heading.text)

# if top_jobs_heading is not None:
#     article = top_jobs_heading.parent
#     if article is not None:
#         for p in article.select('p'):
#             print(re.sub(r'\s{1,}', ' ', p.text).strip())



# PROCURANDO O FORM ----------------
# form_example = parsed_html.select('#footer > div > div.main-header-form > form > fieldset > div > div:nth-child(1)')[0]

# if form_example is not None:
#     original_form = form_example.parent
#     if original_form is not None:
#         for l in original_form.select('label'):
#             print(l)


# PEGANDO CABEÇALHOS DE UMA TABLE --------------
table = parsed_html.select('#pricing > div > div > article > div > table')[0]
# print(table.text)

if table is not None:
    for th in table.select('th'):
        print(th)

print()
print()
print()
print()

# PEGANDO O CONTEUDO DO CONTENT 3
if table is not None:
    for td in table.select('td'):
        if '3' in td.text:
            print(td)

 

