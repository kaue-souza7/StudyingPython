# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive\\Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        new_dir_path = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), 
            dir_
        )
        # print(new_dir_path)
        os.makedirs(new_dir_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), 
            file
        )

        shutil.copy(file_path, new_file_path)
print(NOVA_PASTA)
