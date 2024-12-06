import os
from dotenv import load_dotenv
from toexcel import linha_toexcel, to_excel
from webdriver import chrome_driver, vd_driver

# Carrega as informações delicadas
keys = load_dotenv()

# Variaveis dos caminhos de salvamento dos arquivos
data_base_path = rf"C:\Users\{os.getlogin()}\OneDrive - Veiga e Castro Ltda\Automações\Planilha de Consulta (Cod-Desc)\database"
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


# Captura o arquivo dos endereços
vd_driver(sheets_path, os.getenv('user_login_mab'), os.getenv('pass_login_mab'))
# Converte a planilha para xlsx
linha_toexcel(data_base_path, sheets_path, "MAB")
# Limpa a pasta dnv
remove_file(sheets_path)


# Captura o arquivo dos endereços
vd_driver(sheets_path, os.getenv('user_login_aux'), os.getenv('pass_login_aux'))
# Converte a planilha para xlsx
linha_toexcel(data_base_path, sheets_path, "AUX")
# Limpa a pasta dnv
remove_file(sheets_path)