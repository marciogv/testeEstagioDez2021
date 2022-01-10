"""
Módulo que tem o objetivo de extrair os dados das tabelas que estão inseridas no 'pdf' e criar arquivos 'csv' com estes
mesmos dados

Este módulo só tem a função 'extrair_tabelas_pdf', sendo chamadas outras funções no seu interior. Esta função utiliza
as informações que foram coletados na função anterior do programa para, por meio do módulo 'tabula' percorrer cada uma
das páginas em que foram encontradas tabelas e extrair os dados somente da tabela alvo. 

Utilizada a biblioteca 'tabula' para busca análise das tabelas na página pdf.

Mais detalhes da construção da função são especificados em sua documentação.
"""

import tabula
from src.utils.functions.folder_extrair_tabelas_pdf.tratando_tabela_com_erros import \
    tratando_tabela_com_erros
from src.utils.functions.folder_extrair_tabelas_pdf.descobrir_tabela_pagina_inicial import \
    descobrir_tabela_pagina_inicial
from src.utils.functions.folder_extrair_tabelas_pdf.add_nome_arquivo_csv import add_nome_arquivo_csv


def extrair_tabelas_pdf(arquivo_pdf: str, array_tabelas_completo, read_pdf: object):
    """
    Realiza a extração dos dados das tabelas que serão inseridas no 'pdf' e cria os arquivos 'csv' com estes dados.

    Iniciamos realizando um loop na lista das informações das tabelas, criando variáveis para cada chave-valor do 
    objeto 'tabela'. Fazemos uma condição para saber se a tabela inicia e termina na mesma página, pois isto irá
    modificar a criação dos arquivos 'csv'.

    Caso seja satisfeita, ou seja, inicia e termina na mesma página, colocamos outra condição de ter mais de uma tabela
    na mesma página. Caso isto ocorra será necessário fazer outra análise que a função 'descobrir_tabela_pagina_inicial'
    irá realizar; caso não consideraremos a única tabela da página para análise do conteúdo.
    Chamamos a função 'add_nome_arquivo_csv' que cria um nome para o arquivo 'csv'.
    Em análise manual percebemos que nas duas tabelas que iniciavam e terminavam na mesma página a leitura do 'tabula'
    trazia como retorno um objeto com somente uma coluna, necessitando de uma correção para ser criado o arquivo 'csv'.
    Tal correção é realizada pela função 'tratando_tabela_com_erros'. Criamos então o arquivo 'csv' sem o 'index' para
    não atrapalhar a configuração das colunas do 'csv e colocamos o nome da tabela no array 'lista_arquivos_csv'.

    Caso a condição da tabela iniciar e finalizar na mesma página não seja satisfeita, iniciamos um loop que irá
    percorrer cada uma das páginas onde a tabela está presente. Neste tipo de tabela, na página que ela inicia sempre
    será a tabela[0] da página e nas posteriores a tabela[-1] da página, então só verificamos se é a primeira página
    em que a tabela está presente. Caso esta condição seja satisfeita adicionamos a tabela a um novo arquivo 'csv' sem
    o 'index' e sem 'header' e colocamos o nome da tabela no array 'lista_arquivos_csv'. Caso não seja a primeira 
    página, a tabela será adicionada ao mesmo arquivo criado anteriormente (mode= 'a') e não é necessário tirar o 
    'header'. 
    
    Ao final retornamos o array 'lista_arquivos_csv' que será usado na próxima função do programa.

    Temos como variáveis de função um array vazio ('lista_arquivos_csv') que é preenchido no interior da função.

    :param arquivo_pdf: caminho relativo do arquivo PDF onde se encontram as tabelas alvo
    :type arquivo_pdf: str
    :param array_tabelas_completo: lista com informações das tabelas (nome, numero página inicial e final) que serão 
    utilizados para extrair os dados do arquivo 'pdf'
    :type array_tabelas_completo: list
    :param read_pdf: objeto da biblioteca PyPDF2 com o arquivo PDF a ser analisado
    :type read_pdf: pandas.core.frame.DataFrame


    :return lista_arquivos_csv: lista com nome dos arquivos que serão depois utilizados para criar o arquivo 'zip'
    :rtype lista_arquivos_csv: list
    """
    lista_arquivos_csv = []
    for tabela in array_tabelas_completo:
        pagina_inicial = tabela['pagina_inicio']
        pagina_final = tabela['pagina_final']
        nome_tabela = tabela['tabela']
        tabelas_pagina_inicial = tabula.read_pdf(arquivo_pdf, pages=pagina_inicial)
        qtdade_tabelas_pagina = len(tabelas_pagina_inicial)

        if pagina_final == pagina_inicial:
            if qtdade_tabelas_pagina == 1:
                tabela_atual = tabelas_pagina_inicial[0]
            else:
                indice_tabela = descobrir_tabela_pagina_inicial(read_pdf, nome_tabela, pagina_final,
                                                                qtdade_tabelas_pagina)
                tabela_atual = tabelas_pagina_inicial[indice_tabela]
            nome_arquivo_csv = add_nome_arquivo_csv(tabela_atual)
            tabela = tratando_tabela_com_erros(tabela_atual)
            tabela.to_csv(nome_arquivo_csv, index=False)
            lista_arquivos_csv.append(nome_arquivo_csv)

        else:
            for pagina in range(pagina_inicial, pagina_final + 1):
                tabela_pagina_atual = tabula.read_pdf(arquivo_pdf, pages=pagina)
                if pagina == pagina_inicial:
                    tabela_pagina_atual = tabela_pagina_atual[-1]
                    nome_arquivo_csv = add_nome_arquivo_csv(tabela_pagina_atual)
                    tabela_pagina_atual.to_csv(nome_arquivo_csv, index=False, header=False)
                    lista_arquivos_csv.append(nome_arquivo_csv)
                else:
                    tabela_pagina_atual = tabela_pagina_atual[0]
                    tabela_pagina_atual.to_csv(nome_arquivo_csv, mode='a', index=False)
    return lista_arquivos_csv
