"""
Módulo que tem o objetivo de descobrir qual é a tabela alvo em páginas que contém mais de uma tabela
"""
import re


def descobrir_tabela_pagina_inicial(read_pdf: object, nome_tabela: str, pagina_final: int, 
                                    qtdade_tabelas_pagina: int):
    """
    Realiza análise textual das tabelas da página através de 'identificadores' para descobrir qual se assemelha a tabela
    alvo.
    
    Inicialmente extraimos o texto da página atual e retiramos a quebra de página desta 'str'. Realizamos então uma 
    busca de todas as tabelas da página que que tem nome através da variável 'qtdade_tabelas_com_nome'. É feito um loop
    entre as tabelas encontradas na busca anterior e caso a tabela alvo seja igual a atual testamos uma última condição
    de caso haja uma tabela que finaliza nesta página, o índice da tabela é alvo é o 'index + 1', caso não sera só o
    'index'. Para finalizar somamos um número ao 'index'.

    :param read_pdf: objeto da biblioteca PyPDF2 com o arquivo PDF a ser analisado
    :type read_pdf: PyPDF2.pdf.PdfFileReader
    :param nome_tabela: nome da tabela alvo
    :type nome_tabela: str
    :param pagina_final: número da página final da tabela
    :type pagina_final: int
    :param qtdade_tabelas_pagina: quantidade de tabelas na página atual
    :type qtdade_tabelas_pagina: int

    :return nome_arquivo_csv: posição da tabela alvo entre as tabelas da página atual
    :rtype nome_arquivo_csv: int
    """
    pagina_atual = read_pdf.getPage(pagina_final - 1)
    page_content = pagina_atual.extractText()

    sem_quebra = page_content.replace("\n", "")
    qtdade_tabelas_com_nome = re.findall("(Quadro\s(\w+))", sem_quebra)
    index = 0
    for tabela in qtdade_tabelas_com_nome:
        if tabela[0] == nome_tabela:
            if (len(qtdade_tabelas_com_nome)) == qtdade_tabelas_pagina:
                return index
            else:
                return index + 1
        index += 1
