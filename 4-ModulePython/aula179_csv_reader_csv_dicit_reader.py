# csv.reader e csv.DictReader
# l csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionario
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

CAMINHO_CSV.touch()

with open(CAMINHO_CSV, 'r',encoding="utf8") as file:
    reader = csv.DictReader(file, )
    
    for row in reader:
        print(row['Nome'])