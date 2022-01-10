"""
Módulo que tem o objetivo de criar um nome que será utilizado pela função pai
"""

def add_nome_arquivo_csv(tabela_atual: object):
    """
    Cria um nome (em formato 'str') que será usado para criar o arquivo 'csv'

    No objeto 'pandas' extraído pelo 'tabula na coluna [-1] está presente o nome da tabela, então extraímos esta
    informação e retiramos o esçoa em branco para melhor formatação do nome do arquivo.
    :param tabela_atual: Objeto 'pandas' com a tabela que esta sendo analisada
    :type tabela_atual: object

    :return nome_arquivo_csv: nome do arquivo que será usado para criar o arquivo 'csv'
    :rtype nome_arquivo_csv: str
    """
    coluna = tabela_atual.columns[-1]
    nome_arquivo_csv = coluna.replace(" ", "")
    nome_arquivo_csv = f'{nome_arquivo_csv}.csv'
    return nome_arquivo_csv
