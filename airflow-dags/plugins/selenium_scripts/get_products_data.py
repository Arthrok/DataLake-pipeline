from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import json

# Configurações do navegador remoto
options = webdriver.ChromeOptions()
remote_webdriver = 'http://remote_chromedriver:4444/wd/hub'
driver = webdriver.Remote(command_executor=remote_webdriver, options=options)

browser = driver
baseURL = "https://www.kabum.com.br/"

def searchProduct(product):
    browser.get(baseURL)
    search_bar = browser.find_element(By.ID, "input-busca")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.ENTER)

def collect_product(url):
    browser.get(url)
    title = driver.find_element(By.CLASS_NAME, "sc-58b2114e-6").text
    final_price = driver.find_element(By.CLASS_NAME, "finalPrice").text
    technical_infos = driver.find_element(By.ID, "technicalInfoSection").text
    date_collect = datetime.today().strftime("%Y-%m-%d")

    product_info = {
        "title": title,
        "final_price": final_price,
        "technical_infos": technical_infos,
        "date_collect": date_collect
    }
    return product_info

def select_product():
    products_info = []
    products = browser.find_elements(By.CLASS_NAME, "productCard")
    links = []
    for product in products:
        link_element = product.find_element(By.TAG_NAME, "a")
        link = link_element.get_attribute("href")
        links.append(link)

    for link in links:
        product_info = collect_product(link)
        products_info.append(product_info)

    return products_info

def get_products_data():
    searchProduct("placa de video")
    products = select_product()

    driver.quit()

    return json.dumps(products)

