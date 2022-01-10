"""
Módulo que inicia o webdriver do Chrome no selenium, faz as suas configurações e executa as ações de entrar no site
alvo, entrando nas páginas e realizando o download do arquivo PDF

Duas funções no módulo: 'entrando_paginas' entra na página principal, clica no cookie e passa para a próxima página
alvo; executando_funcoes' executa a função acima e todas as outras do programa que irá navegar pelo site até chegar na
página que tem o link do 'pdf' que será baixado.

Temos como variáveis 'root_folder', 'arquivo_driver', 'pasta_pdf', 'caps' e 'driver'. 'caps' é a configuração do 
'webdriver' para não aguardar o carregamento completo da página e 'driver' é o objeto do navegador que vai executar 
as ações requisitadas.

Utilizada a biblioteca 'selenium' que executa o navegador e 'os' para busca dos caminhos relativos.

Mais detalhes da construção da função são especificados em sua documentação.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from src.utils.functions.abrindo_mudando_aba import abrindo_nova_aba_pdf
from src.utils.functions.download_pdf import download_pdf


# Caminho para a raiz do projeto
root_folder = os.getcwd()

# Caminho para a pasta chromedriver
arquivo_driver = os.path.join(root_folder, 'bin', 'chromedriver')

# Caminho para a pasta download -> pdf
pasta_pdf = os.path.join(root_folder, 'src', 'files', 'pdf', 'padrao_tiss_componente_organizacional.pdf')


caps = DesiredCapabilities().CHROME

caps["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(arquivo_driver, desired_capabilities=caps)


def entrando_paginas(driver: webdriver.Chrome):
    """
    Entra na página principal do site alvo e realiza navegação até a página onde está hospedado o arquivo 'pdf' alvo

    Primeiramente entramos na página principal do site alvo, chamamos o objeto 'WebDriverWait' do 'selenium' para que
    possamos esperar que o link do cookie esteja pronto para ser clicado e clicamos nele. Usamos 'try' e 'except' para
    o caso de certo 'bug' que as vezes ocorre de o cookie estar carregado mas não ser reconhecido pelo WebDriver. Neste
    caso forçamos no 'except' ele clicar no link.
    Após isto entramos na próxima página que é onde teremos o link para baixar o arquivo 'pdf'.

    :param driver: objeto do webdriver que executa o navegador
    :type driver: webdriver.Chrome
    """
    try:
        driver.get("https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss")
        wait = WebDriverWait(driver, 3)
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'lcb-botao'))).click()
    except ElementClickInterceptedException as e:
        print(e)
        cookie_button = driver.find_element(By.CLASS_NAME, 'lcb-botao')
        cookie_button.click()
    last_TISS_version = driver.find_element(By.CLASS_NAME, 'alert-link')
    last_TISS_version.click()

def executando_funcoes(driver):
    """
    Controle central para execução do programa

    Primeiramente com a função 'entrando_paginas' entramos na página principal e seguimos com as ações para chegar até
    a página que contém o lnik do download do 'pdf'; com a função 'abrindo_nova_aba_pdf' abrimos a url do 'pdf' e
    seguimos para a aba aberta (configuralçao da página); então realizamos o download do 'pdf' e realizamos uma cópia[
    para a pasta do programa que irá extrair suas informações; por último fechamos o navegador.
    :param driver: objeto do webdriver que executa o navegador
    :type driver: webdriver.Chrome
    """
    entrando_paginas(driver)
    caminho_url_pdf = abrindo_nova_aba_pdf(driver)
    download_pdf(caminho_url_pdf, pasta_pdf)
    driver.quit()

if __name__ == '__main__':
    executando_funcoes(driver)
