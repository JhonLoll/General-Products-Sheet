import os
from toexcel import to_excel
from webdriver import chrome_driver

# Variaveis dos caminhos de salvamento dos arquivos
data_base_path = r"C:\Desenvolvimento\General-Products-Sheet\database"
sheets_path = r"C:\Desenvolvimento\General-Products-Sheet\sheets"

# Função para remover os arquivos presentes na pasta Sheets
def remove_file(sheets_path):
    path = sheets_path
    dir = os.listdir(path)

    for file in dir:
        os.remove(os.path.join(sheets_path, file))

# === Funções Gerais ===
# Realiza a captura do arquivo no Chrome
chrome_driver(sheets_path)
# Converte o arquivo para xlsx e salva apenas cod e desc em um arquivo database
to_excel(data_base_path, sheets_path)
# Remove os arquivos da pasta informada
remove_file(sheets_path)