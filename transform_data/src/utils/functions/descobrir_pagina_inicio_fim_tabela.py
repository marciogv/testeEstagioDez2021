"""
Módulo que tem o objetivo de descobrir  número da página inicial e final de uma cada das tabelas alvo dentro do arquivo
PDF em que estão inseridas

Este módulo só tem a função 'descobrir_pagina_inicio_fim_tabela' que vai realizar uma busca textual nas páginas do 
arquivo PDF para descobrir em que página se encontra o início e fim das tabelas em questão.

Utilizada a biblioteca 'tabula'  para busca e análise das tabelas na página pdf e a biblioteca 're' para busca textual no
arquivo pdf através de expressões regulares.

Mais detalhes da construção da função são especificados em sua documentação.
"""

import tabula
import re


def descobrir_pagina_inicio_fim_tabela(arquivo_pdf: str, read_pdf, number_of_pages: int,
                                       array_tabelas: list):
    """
    Realiza uma busca textual nas páginas do arquivo PDF para descobrir em que página se encontra o início e fim das
    tabelas em questão.

    Iniciamos realizando um loop na lista das tabelas a serem encontradas e outro loop interno nas páginas do arquivo
    PDF, assim buscaremos em cada página do arquivo PDF cada uma das tabelas em questão. Em cada página extraimos o
    texto total (em formato 'str') e retiramos as quebras de linhas que atrapalham na busca textual. Temos a primeira
    condição de 'caso encontre o texto na página' (busca textual em 'str') e 'existir uma tabela nesta página' (verificação
    feita pelo tabula) adicione o número de página inicial e modifique para 'True' a variavel 'entrou_na_tabela'. Por
    uma questão de desempenho a condição de 'existir a tabela na página' é colocada dentro da condição de 'encontrar o
    texto' (a análise do tábula é onerosa em sua execução).
    Temos então a ação de buscar a 'página final' da tabela. Para encontrar usamos dois tipos diferentes de
    identificadores de fim da tabela: 1) 'nome da tabela' (...) 'Fonte:' - que indica que a tabela inicia e finaliza na
    mesma página; 2) e só 'Fonte:' que vai indicar o fim da tabela no caso de não estar na mesma página do início.
    Colocamos então a condição de encontrar o primeiro identificador: se satisfeito, muda para 'False' a variável
    'entrou na tabela'; caso não atribui o valor 'True' para variável 'multiplas_páginas' e segue para a próxima volta
    do laço, permitindo que caso o segundo identificador seja satisfeito, seja atribuiodo o valor para a 'pagina_final'.


    Temos como variáveis de função um array com diversos objetos que contem o nome de cada tabela e a página inicial e
    final, e outras duas variáveis que servem como parâmetro de condições internas.

    :param arquivo_pdf: caminho relativo do arquivo PDF onde se encontram as tabelas alvo
    :type arquivo_pdf: str
    :param read_pdf: objeto da biblioteca PyPDF2 com o arquivo PDF a ser analisado
    :type read_pdf: PyPDF2.pdf.PdfFileReader
    :param number_of_pages: número de páginas do arquivo PDF
    :type number_of_pages: int
    :param array_tabelas: lista com nome das tabelas (em formato 'str') que serão buscadas no arquivo PDF
    :type array_tabelas: list

    :return array_tabelas_completo: lista com objetos que contém as informações de cada tabela, como nome, página
    inicial e página final
    :rtype array_tabelas_completo: list
    """
    array_tabelas_completo = []
    entrou_na_tabela = False
    multiplas_paginas = False

    for tabela in array_tabelas:
        for pagina in range(number_of_pages):
            numero_pagina_atual = pagina + 1
            pagina_atual = read_pdf.getPage(pagina)
            page_content = pagina_atual.extractText()
            sem_quebra = page_content.replace("\n", "")

            if tabela in sem_quebra:
                tabelas_pagina = tabula.read_pdf(arquivo_pdf, pages=numero_pagina_atual)
                if len(tabelas_pagina) == 0:
                    continue
                array_tabelas_completo.append({'tabela':tabela, 'pagina_inicio':numero_pagina_atual})
                entrou_na_tabela = True

            if entrou_na_tabela:
                string_fim_tabela = sem_quebra.find("Fonte:")
                tabela_comeco_fim_mesma_pagina = re.findall(f"({tabela})(?s:.*?)(Fonte:)", sem_quebra)
                if (multiplas_paginas and string_fim_tabela != -1) or ((len(tabela_comeco_fim_mesma_pagina)) != 0):
                    array_tabelas_completo[-1]['pagina_final'] = numero_pagina_atual
                    entrou_na_tabela = False
                else:
                    multiplas_paginas = True
                    continue
    return array_tabelas_completo

