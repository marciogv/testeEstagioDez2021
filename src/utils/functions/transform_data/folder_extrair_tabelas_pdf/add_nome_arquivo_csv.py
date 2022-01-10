
def add_nome_arquivo_csv(tabela_atual):
    coluna = tabela_atual.columns[-1]
    nome_arquivo_csv = coluna.replace(" ", "")
    nome_arquivo_csv = f'{nome_arquivo_csv}.csv'
    return nome_arquivo_csv
