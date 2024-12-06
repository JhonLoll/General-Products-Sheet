import os
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

def linha_toexcel(database_path, sheets_path, city):
    # Captura o nome do arquivo que está na pasta
    for arquivo in os.listdir(sheets_path):
        nome_arquivo = arquivo

    # Realiza a conversão de xls para xlsx para que o pandas consiga trabalhar com a planilha
    df = pd.read_excel(sheets_path + "/" + nome_arquivo, header=None)
    df.to_excel(database_path + f'/Linha_de_Separacao_{city}.xlsx', index=False, header=False)

    # Carregar a planilha
    file_path = f"{database_path}/Linha_de_Separacao_{city}.xlsx"  # caminho do arquivo
    df = pd.read_excel(file_path)

    # Criar uma lista para armazenar novas linhas
    new_rows = []

    # Iterar pelas linhas do DataFrame
    for index, row in df.iterrows():
        codes = str(row["Codigo Material"]).split(";")
        
        if len(codes) > 1:  # Verificar se existem múltiplos códigos
            # Manter o primeiro código na linha atual
            df.at[index, "Codigo Material"] = codes[0]
            
            # Criar uma nova linha para cada código adicional
            for code in codes[1:]:
                new_row = row.copy()
                new_row["Codigo Material"] = code
                new_rows.append(new_row)

    # Adicionar as novas linhas ao DataFrame
    if new_rows:
        new_rows_df = pd.DataFrame(new_rows, columns=df.columns)
        df = pd.concat([df, new_rows_df], ignore_index=True)

    # Salvar o resultado em um novo arquivo Excel
    output_file_path = f"{database_path}/Linha_de_Separacao_{city}.xlsx"
    df.to_excel(output_file_path, index=False)