import json
from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python_operator import PythonOperator

from airflow.providers.mongo.hooks.mongo import MongoHook

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
options.add_argument('--headless')  # Opcional, se você não quer ver o navegador
options.add_argument('--no-sandbox')  # 
driver = webdriver.Chrome(executable_path=r'/opt/airflow/chromedriver', options=options)

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

def main():
    searchProduct("placa de video")
    products = select_product()

    driver.quit()

    return json.dumps(products)



default_args = {
    "owner": "Arthur",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
    "start_date": datetime(2024, 5, 6)
}

@dag(
    schedule_interval='0 23 * * *',
    default_args=default_args,
    description='DAG to extract product data using Selenium and store in MongoDB',
    tags=['product_extraction', 'selenium', 'mongo'],
    catchup=False,
    dag_id='etl_products'
)
def etl_products():
    @task(execution_timeout=timedelta(minutes=30))
    def extract_data():
        """Fetch data using Selenium and return as JSON."""
        product_data = main()
        print(product_data)
        return product_data


    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    screp = extract_data()


    start >> screp >> end

dag_instance = etl_products()

