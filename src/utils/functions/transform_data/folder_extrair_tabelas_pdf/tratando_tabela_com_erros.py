

# Lendo tabelas com erros no Tabula
def tratando_tabela_com_erros(tabela):
    primeira_coluna = tabela.iloc[:, 0]
    new = primeira_coluna.str.split(" ", n=1, expand=True)
    tabela["Código"] = new[0]
    tabela["Descrição da categoria"] = new[1]

    tabela.drop(tabela.columns[0], axis=1, inplace=True)
    tabela = tabela.dropna()
    tabela = tabela.iloc[1:, :]
    return tabela