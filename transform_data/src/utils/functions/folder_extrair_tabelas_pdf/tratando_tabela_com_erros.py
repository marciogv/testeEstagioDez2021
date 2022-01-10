"""
Módulo que tem o objetivo de corrigir um erro de extração da tabela alvo para que a mesma esteja adequada para inserção
em arquivo 'csv'
"""
def tratando_tabela_com_erros(tabela):
    """
    Realiza tratamento das colunas da tabela alvo caso tenha apenas uma coluna

    Nesta função dividimos a coluna da tabela em dois através do separador ' ', criamos duas novas colunas, chamadas de
    'Código' e 'Descrição da categoria' e excluímos a coluna original, retornando a nova tabela modificada.

    :param tabela: objeto da biblioteca 'pandas' com tabela a ser analisada
    :type tabela: pandas.core.frame.DataFrame

    :return tabela: nova tabela modificada
    :rtype tabela: pandas.core.frame.DataFrame
    """
    primeira_coluna = tabela.iloc[:, 0]
    new = primeira_coluna.str.split(" ", n=1, expand=True)
    tabela["Código"] = new[0]
    tabela["Descrição da categoria"] = new[1]

    tabela.drop(tabela.columns[0], axis=1, inplace=True)
    tabela = tabela.dropna()
    tabela = tabela.iloc[1:, :]
    return tabela
