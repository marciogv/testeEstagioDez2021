"""
Módulo que entra na página que hospeda o arquivo 'pdf' alvo, abre o 'pdf' em nova aba e realiza a troca da página
principal do navegador para a nova aba criada e extrai sua url.

Duas funções no módulo: 'abrindo_nova_aba_pdf' clica no link para fazer o download do arquivo 'pdf', aguarda a nova aba
ser aberta e chama a função 'changing_page'; 'changing_page' vai mudar a página principal para a do arquivo 'pdf'
e retornar a url desta nova aba.

Utilizada a biblioteca 'selenium' que executa o navegador e 'time' para fazer o sistema 'dormir' por uns segundos.

Mais detalhes da construção da função são especificados em sua documentação.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


def changing_page(main_browser, original_window):
    """
    Realiza a troca da aba principal do navegador e apresenta a url desta

    Fazemos um loop sobre a lista de janelas do navegador. Visto que só temos duas abas, caso a janela atual do loop
    seja a original, trocamos a página principal para a seguinte e retornamos a url da nova aba.

    :param main_browser: objeto do webdriver que executa o navegador
    :type main_browser: webdriver.Chrome
    :param original_window: objeto do webdriver que executa o navegador
    :type original_window: webdriver.Chrome

    :return main_browser.current_url: lista com objetos que contém as informações de cada tabela, como nome, página
    inicial e página final
    :rtype main_browser.current_url: str
    """
    for window_handle in main_browser.window_handles:
        if window_handle != original_window:
            main_browser.switch_to.window(window_handle)
            return main_browser.current_url


def abrindo_nova_aba_pdf(main_browser):
    """
    Função que abre aba do 'pdf', aguarda o navegador estar com duas abas e chama a função para trocar a aba

    Chamamos o objeto 'WebDriverWait' do 'selenium' para que possamos esperar que o link do download esteja pronto para
    ser clicado e clicamos nele. Usamos 'try' e 'except' para o caso de certo 'bug' que as vezes ocorre de o cookie
    estar carregado mas não ser reconhecido pelo WebDriver. Neste caso forçamos no 'except' ele clicar no link.
    Deixamos o sistema 'dormir' por 1 segundo para que o navegador espere a aba ser aberta.

    Esperamos então que o navegador apresente duas abas abertas e chamamos a função para mudar a aba principal do
    navegador.

    :param main_browser: objeto do webdriver que executa o navegador
    :type main_browser: webdriver.Chrome

    :return changing_page: executamos a função que irá retornar uma 'str' com a url da página de download
    :rtype changing_page: function
    """
    wait = WebDriverWait(main_browser, 2)
    original_window = main_browser.current_window_handle
    assert len(main_browser.window_handles) == 1
    try:
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn'))).click()
    except ElementClickInterceptedException as e:
        button = main_browser.find_element(By.CLASS_NAME, 'btn')
        button.click()
    sleep(1)
    wait.until(ec.number_of_windows_to_be(2))
    return changing_page(main_browser, original_window)
