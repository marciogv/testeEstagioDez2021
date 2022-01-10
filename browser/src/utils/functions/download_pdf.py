"""
Módulo que realiza o download do arquivo 'pdf' e o copia para uma pasta no programa que irá consumir este 'pdf'.

Este módulo só tem uma função que iré realizar o download e cópia do arquivo 'pdf' da internet.

Utilizada a biblioteca 'request' para fazer o download do arquivo do site, 'os' para busca dos caminhos relativos e
'shutil' para copiar o arquivo 'pdf' para outra pasta do sistema.

Mais detalhes da construção da função são especificados em sua documentação.
"""

import requests
import os
import shutil

# Caminho para a raiz do projeto
root_folder = os.getcwd()

# Caminho para a raiz do programa que irá realizar a análise do arquivo 'pdf'
up_root_folder = os.path.dirname(os.getcwd())

# Caminho para a pasta alvo onde o arquivo 'pdf' será copiado
nova_pasta = os.path.join(up_root_folder, 'transform_data', 'src', 'files', 'pdf',
                          'padrao_tiss_componente_organizacional.pdf')

def download_pdf (caminho_url_pdf, arquivo_pc_pdf):
    """
    Realiza o download do arquivo 'pdf' e sua cópia para outra pasta do sistema.

    Realizamos a requisição do arquivo a partir da paǵina 'url, abrimos um novo arquivo 'pdf' no sistema e escrevemos
    a resposta obtida. Copiamos então este novo arquivo para uma pasta dentro do programa que irá relizar análise deste
    arquivo 'pdf'.

    :param caminho_url_pdf: url do arquivo 'pdf' que será baixado
    :type caminho_url_pdf: str
    :param arquivo_pc_pdf: caminho onde o arquivo será baixado no computador
    :type arquivo_pc_pdf: str
    """
    resposta = requests.get(caminho_url_pdf)
    with open (arquivo_pc_pdf, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
        print('Fez download!')
    nova_pasta = os.path.join(up_root_folder, 'transform_data', 'src', 'files', 'pdf',
                              'padrao_tiss_componente_organizacional.pdf')
    shutil.copyfile(arquivo_pc_pdf, nova_pasta)
