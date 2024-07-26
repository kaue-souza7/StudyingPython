from pathlib import Path
import shutil

home = Path.home()

# caminho_arquivo = Path().absolute()
# print(caminho_arquivo)

path = Path(__file__).parent
# print(path.parent)

# new_path = path / 'arquivo.txt'
# print(new_path)

path_file = Path.home() / 'OneDrive/Área de Trabalho' / 'arquivo.txt'
path_file.touch()
path_file.write_text('''Olá Mundo, 
        I want a present, because i don't have!
''')
print(path_file.read_text())
path_file.unlink()


caminho_pasta = Path.home() / 'OneDrive/Área de Trabalho' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)

new_folder = caminho_pasta / 'New Folder'
new_folder.mkdir(exist_ok=True)

other_file = new_folder / 'arquivo.txt'
other_file.touch()
other_file.write_text('HI, How are you World')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('HI, How are you World?')

# caminho_pasta.rmdir()
# print(shutil.rmtree(caminho_pasta))

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)


for i in range(1, 11):
    file = files / f'arquivo{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with open(file, 'a+') as text_file:
        text_file.write('HELLO BEE\r\n')
        text_file.write(f'file_{i}.txt')

# FUNÇÃO RECURSIVA PARA APAGAR A PASTA
# DEVE-SE APAGAR PRIMEIRO OS ARQUIVOS DE CADA PASTA DEPOIS AS PASTA

# A FUNÇÃO PASSA POR CADA ARQUIVO DO CAMINHO RECEBIDO, SE FOR PASTA
# ELA ENTRA E PROCURA ARQUIVO PARA APAGAR, SE ESSE PASTA TIVER OUTRA
# PASTA A FUNÇÃO ENTRA E APAGA OS ARQUIVOS.

# PARA ISSO, COMO É UMA FUNÇÃO RECURSIVA, ELA CHAMA ELA MESMA,
# QUANDO ENCONTRA UMA PASTA PASSANDO O NOVO CAMINHO PARA ELA MESMA
# ASSIM ENTÃO ENTRANDO NA PASTA E APAGANDO O FILES.


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()
    
    if remove_root:
        root.rmdir()



rmtree(caminho_pasta)


    # file.touch()
    # file.write_text(f'Este arquivo é o arquivo de número: {i}')