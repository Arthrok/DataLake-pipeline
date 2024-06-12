#!/usr/bin/env bash

# Atualiza os repositórios e instala wget e unzip
apt-get update
apt-get install -y wget unzip

# Determina a versão mais recente do ChromeDriver
CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)

# Baixa e instala o ChromeDriver
wget -N "http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" -P /opt/airflow/
unzip /opt/airflow/chromedriver_linux64.zip -d /opt/airflow/
rm /opt/airflow/chromedriver_linux64.zip
chown root:root /opt/airflow/chromedriver
chmod 0755 /opt/airflow/chromedriver
