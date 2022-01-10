"""
Módulo que cria um arquivo 'zip' contendo os arquivos 'csv' criado na função anterior do programa, o transfere para
outra pasta.

Utilizada biblioteca 'os' para busca do caminho relativo dos arquivos no sistema operacional, 'zipfile' para compactação
de arquivos em 'zip' e 'shutil' para mover arquivos no sistema.

Cria o arquivo 'zip', o transfere para uma outra pasta e posteriormente apaga os arquivos 'csv'
"""
import zipfile
import os
import shutil


def criando_arquivo_zip(root_folder: str, arquivos_csv: list):
    """
    Cria um arquivo 'zip', insere nele os arquivos 'csv' criado anteriormente, transfere o 'zip' para outra pasta e
    depois apaga os arquivos 'csv'

    Inicialmente criamos um novo arquivo 'zip', depois realizamos um loop sobre o nome dos arquivos 'csv', inserindo
    cada dentro do 'zip' e o apagando. Fechamos o arquivo 'zip' e o transferimos para outra pasta.

    :param root_folder: nome da pasta raiz do projeto
    :type root_folder: str
    :param arquivos_csv: lista com nome dos arquivos 'csv'
    :type arquivos_csv: list
    """
    z = zipfile.ZipFile('Teste_{Marcio_Vieira}.zip', 'w', zipfile.ZIP_DEFLATED)
    for arquivo in arquivos_csv:
        z.write(arquivo)
        os.remove(arquivo)
    z.close()
    src_file_root = os.path.join(root_folder, 'Teste_{Marcio_Vieira}.zip')
    src_file_dst = os.path.join(root_folder, 'src', 'files', 'csv', 'Teste_{Marcio_Vieira}.zip')
    shutil.move(src_file_root, src_file_dst)
