from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
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