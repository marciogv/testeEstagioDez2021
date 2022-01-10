import requests


def download_pdf (caminho_url_pdf, arquivo_pc_pdf):
    resposta = requests.get(caminho_url_pdf)
    with open (arquivo_pc_pdf, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
        print('Fez download!')