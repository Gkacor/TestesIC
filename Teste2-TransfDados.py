from tabula import convert_into
import zipfile
import os

#Trocar C: pelo caminho da pasta onde estão os arquivos PDF.
table_file = r"C:\PycharmProjects\ProjetoIntuitiveCare\Anexo1.pdf"
output_csv = r"C:\PycharmProjects\ProjetoIntuitiveCare\Anexo1Tabelas.csv"

df = convert_into(table_file, output_csv, output_format='csv', lattice=True, stream=False, pages="all")

teste_zip = zipfile.ZipFile('C:\\PycharmProjects\\ProjetoIntuitiveCare\\Teste2.zip', 'w')
for folder, subfolders, files in os.walk('C:\\PycharmProjects\\ProjetoIntuitiveCare'):
    for file in files:
        if file.endswith('.csv'):
            teste_zip.write(os.path.join(folder, file),
                             os.path.relpath(os.path.join(folder, file),
                             'C:\\PycharmProjects\\ProjetoIntuitiveCare'),
                             compress_type = zipfile.ZIP_DEFLATED)
teste_zip.close()