"""
Módulo que centraliza as ações do programa que tem o objetivo extrair tabelas de um arquivo PDF, transformar em
arquivos 'csv' que serão zipados em um mesmo arquivo

Este módulo tem somente uma função 'executar_tarefas' que executa funções de outros três módulos que extraem os dados
de três tabelas inseridas em um arquivo PDF, criam arquivos 'csv' com estes dados e comprimem os arquivos em um 'zip'.
Tivemos que dividir a ação de extração dos dados das tabelas no arquivo PDF em dois processos diferentes: 1- transformar
as páginas do PDF em 'str (através do PyPDF2) para realizar busca textual com identificadores das tabelas
(EX: 'Quadro 30'), descobrindo a página que iniciam e terminam; 2- extrair os dados das tabelas (através do tabula).
Isto foi necessário pois o 'tabula' não identifica o que se encontra acima e embaixo da tabela - no caso seu nome e
legenda e somente ele consegue transformar os dados em uma tabela 'csv'.

Temos como variáveis 'root_folder', 'arquivo_pdf', 'pdf_file', 'read_file', 'number_of_pages' e 'array_tabelas' que é
uma lista com os identificadores das tabelas.
Utilizada biblioteca 'PyPDF2' para a leitura do arquivo 'pdf e a biblioteca 'os' para busca do caminho relativo dos 
arquivos no sistema operacional.

Mais detalhes da construção da função são especificados em sua documentação.
"""

import os
import PyPDF2

from src.utils.functions.descobrir_pagina_inicio_fim_tabela import descobrir_pagina_inicio_fim_tabela
from src.utils.functions.extrair_tabelas_pdf import extrair_tabelas_pdf
from src.utils.functions.criando_arquivo_zip import criando_arquivo_zip

# Caminho para a raiz do projeto
root_folder = os.getcwd()

# Caminho para a pasta download -> pdf
arquivo_pdf = os.path.join(root_folder, 'src', 'files', 'pdf', 'padrao_tiss_componente_organizacional.pdf')

pdf_file = open(arquivo_pdf, 'rb')

#Faz a leitura usando a biblioteca PYPDF
read_pdf = PyPDF2.PdfFileReader(pdf_file)

#Pega o numero de páginas da página PDF
number_of_pages = read_pdf.getNumPages()

array_tabelas = ["Quadro 30", "Quadro 31", "Quadro 32"]


def executar_tarefas():
    """
    Controle central para execução do programa

    Primeiramente executa a função que irá descobrir o número da página inicial e final de cada tabela, depois executa
    a função que vai extrair os dados das tabelas do arquivo PDF e criar os arquivos 'csv' de cada tabela e por último
    executa a função que cria um arquivo 'zip' com todos os arquivos 'csv' e transfere para a pasta 'files/csv'

    """
    array_tabelas_completo = descobrir_pagina_inicio_fim_tabela(arquivo_pdf, read_pdf, number_of_pages, array_tabelas)
    lista_arquivos_csv = extrair_tabelas_pdf(arquivo_pdf, array_tabelas_completo, read_pdf)
    criando_arquivo_zip(root_folder, lista_arquivos_csv)

if __name__ == '__main__':
    executar_tarefas()
