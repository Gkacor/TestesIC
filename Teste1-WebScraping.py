import requests
from bs4 import BeautifulSoup
import zipfile
import os

url = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
i = 0

for link in links:
    if ("Anexo" in link.get('href', [])):
        i += 1

        print("Baixando arquivo: ", i)

        response = requests.get(link.get('href'))
        anexos = open("Anexo" + str(i) + (".pdf"), 'wb')
        anexos.write(response.content)
        anexos.close()

        print("Arquivo ", i, " Baixado")
print("Todos os arquivos PDF foram baixados.")

#Trocar C: pelo caminho da pasta onde estão os arquivos PDF.
#Deixar o "Anexos.zip". O arquivo zip será criado na mesma pasta.
anexos_zip = zipfile.ZipFile('C:\\PycharmProjects\\ProjetoIntuitiveCare\\Anexos.zip', 'w')
for folder, subfolders, files in os.walk('C:\\PycharmProjects\\ProjetoIntuitiveCare'):
    for file in files:
        if file.endswith('.pdf'):
            anexos_zip.write(os.path.join(folder, file),
                             os.path.relpath(os.path.join(folder, file),
                             'C:\\PycharmProjects\\ProjetoIntuitiveCare'),
                             compress_type = zipfile.ZIP_DEFLATED)
anexos_zip.close()

print("Todos os arquivos PDF foram salvos em um .zip.")

