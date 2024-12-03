# Biblioteca para trabalhar excel
import pandas as pd

def to_excel(database_path, sheets_path):
    # Realiza a conversão de xls para xlsx para que o pandas consiga trabalhar com a planilha
    df = pd.read_excel(sheets_path + '/relatorioSaldoEstoque.xls', header=None)
    df.to_excel(sheets_path + '/relatorioSaldoEstoque.xlsx', index=False, header=False)

    # Carregar a planilha no DataFrame
    df = pd.read_excel(sheets_path + '/relatorioSaldoEstoque.xlsx', header=None)

    # Array para armazenar as informações do split
    dados = []

    # Iterar sobre a coluna B
    for index, value in df[1].items():
        if pd.notna(value):  # Verifica se a célula não está vazia
            value = value.split('-', 1)
            if len(value) >= 2:
                dados.append(
                    {
                        'CODIGO': value[0],
                        'DESCRICAO': value[1]
                    }
                )

    pd.DataFrame(dados).to_excel(database_path + '/database_cod_desc.xlsx')

