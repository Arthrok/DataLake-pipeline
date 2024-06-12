FROM apache/airflow:2.9.0

USER root
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD install_chrome_chromedriver.sh .
RUN sh install_chrome_chromedriver.sh

# Switch to airflow user before installing Python packages
USER airflow
ADD requirements.txt .
RUN pip install --upgrade setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt
