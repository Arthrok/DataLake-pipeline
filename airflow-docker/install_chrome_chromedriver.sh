#!/usr/bin/env bash

# Atualiza os repositórios e instala wget e unzip
apt-get update
apt-get install -y wget unzip

# Determina a versão mais recente do ChromeDriver
CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)


curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get -y update
apt-get -y install google-chrome-stable

# Baixa e instala o ChromeDriver
wget -N "http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" -P /opt/airflow/
unzip /opt/airflow/chromedriver_linux64.zip -d /opt/airflow/
rm /opt/airflow/chromedriver_linux64.zip
chown root:root /opt/airflow/chromedriver
chmod 0755 /opt/airflow/chromedriver
