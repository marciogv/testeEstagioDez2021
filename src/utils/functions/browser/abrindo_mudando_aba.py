from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def changing_page(main_browser, original_window):
    for window_handle in main_browser.window_handles:
        if window_handle != original_window:
            main_browser.switch_to.window(window_handle)
            print('Mudou pagina!')
            return main_browser.current_url


def abrindo_nova_aba_pdf(main_browser):
    wait = WebDriverWait(main_browser, 10)
    original_window = main_browser.current_window_handle
    assert len(main_browser.window_handles) == 1
    organizational_component = main_browser.find_element(By.CLASS_NAME, 'btn').click()
    wait.until(EC.number_of_windows_to_be(2))
    return changing_page(main_browser, original_window)