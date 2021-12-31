from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser

def changing_page(main_browser, original_window):
    for window_handle in main_browser.window_handles:
        if window_handle != original_window:
            main_browser.switch_to.window(window_handle)
            return main_browser.current_url

def entrando_pagina_padrao_TISS(main_browser):
    cookie_button = main_browser.find_element(By.CLASS_NAME, 'lcb-botao')
    sleep(2)
    cookie_button.click()
    last_TISS_version = main_browser.find_element(By.CLASS_NAME, 'alert-link')
    last_TISS_version.click()

def abrindo_nova_aba_pdf(main_browser):
    wait = WebDriverWait(main_browser, 10)
    original_window = main_browser.current_window_handle
    assert len(main_browser.window_handles) == 1
    organizational_component = main_browser.find_element(By.CLASS_NAME, 'btn').click()
    wait.until(EC.number_of_windows_to_be(2))
    return changing_page(main_browser, original_window)

def download_pdf (caminho_url_pdf, arquivo_pc_pdf):
    resposta = requests.get(caminho_url_pdf)
    with open (arquivo_pc_pdf, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)

if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    main_browser = browser.get('https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss')
    entrando_pagina_padrao_TISS(browser)
    caminho_url_pdf = abrindo_nova_aba_pdf(browser)

    download_pdf(caminho_url_pdf, 'test.pdf')
    sleep(3)
    # browser.quit()

'''

Coisas a fazer:
    - Arrumar bug que as vezes não fecha o cookie e continua no programa
    - Fechar o browser após fazer o download ou nem abrir o browser para ganho de desempenho

'''