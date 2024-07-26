# json.dumo e json.load com arquivos
import json
import os



FILE_NAME = 'aula177.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

print(CAMINHO_ABSOLUTO_ARQUIVO)
print()
# print(__file__)

movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
    'is_movie': True, 
    'imdb_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as file:
    json.dump(
        movie, 
        file,
        ensure_ascii=False, 
        indent=1
    )

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as file:
    movie_of_json = json.load(file)
    print(movie_of_json)


# print(movie)
