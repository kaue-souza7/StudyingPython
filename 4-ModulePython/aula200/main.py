# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python

from PIL import Image
from pathlib import Path
from typing import Type

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original2.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new2.jpg'

# Carregando Imagem
pil_image = Image.open(ORIGINAL)

width, heigth = pil_image.size
# exif = pil_image.info['exif']

# width     new_width
#height     X

new_width = 2160
new_heigth = round(heigth * new_width / width)

new_image = pil_image.resize(size=(new_width, new_heigth))
new_image.save(
        NEW_IMAGE,
        optimize=True, 
        quality=70
    )

# print(width, heigth)
# print(new_width, new_heigth)