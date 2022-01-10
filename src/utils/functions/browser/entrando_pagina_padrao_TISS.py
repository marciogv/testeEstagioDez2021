from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


def entrando_pagina_padrao_tiss(main_browser):
    wait = WebDriverWait(main_browser, 3)
    # main_browser.delete_all_cookies()
    # print(main_browser.get_cookies())
    cookie_button = main_browser.find_element(By.CLASS_NAME, 'lcb-botao')
    sleep(2)
    cookie_button.click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lgpd-cookie-banner-janela"]/div[2]/button'))).click()
    # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '.lcb-botao'))).click()
    last_TISS_version = main_browser.find_element(By.CLASS_NAME, 'alert-link')
    last_TISS_version.click()
    print('Entrou na pagina TISS')
