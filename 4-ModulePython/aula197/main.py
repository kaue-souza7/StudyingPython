from pathlib import Path
from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
ORIGANALS_FOLDER = PASTA_RAIZ / 'pdfs_originais'
NEW_FOLDER = PASTA_RAIZ / 'new_files'

RELATORIO_BACEN = ORIGANALS_FOLDER / 'exemplo2.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

# print(page0.extract_text())
print(len(reader.pages))
page0 = reader.pages[0]
imagem0 = page0.images[0]
print(len(page0.images))

for image in page0.images:
    with open(NEW_FOLDER / image.name, 'wb') as fp:
        fp.write(imagem0.data)


# ---> AQUI ESCREVE PAGINA POR PÁGINA NA PASTA <---
# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     writer.add_page(page0)

#     with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as file:
#         writer.write(file)

# --> AQUI ESCREVE PAGINA POR PAGINA EM UM SÓ PDF (REESCREV O PDF) <---
writer = PdfWriter()

with open(NEW_FOLDER / 'NovoPDF.pdf', 'wb') as file:
    for page in reader.pages:
        writer.add_page(page)

    writer.write(file)

merger = PdfMerger()
amount_page = 21

for i in range(amount_page):
    merger.append(NEW_FOLDER / f'page{i}.pdf')

merger.write(NEW_FOLDER /  'MERGED.pdf')
merger.close()