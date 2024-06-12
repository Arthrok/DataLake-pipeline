# DataLake-pipeline

## Descrição
Este projeto implementa uma pipeline de Data Lake utilizando Apache Airflow para agendar extrações de dados de plataformas de venda de componentes eletrônicos usando Selenium. O objetivo é transformar esses dados em várias etapas, seguindo a classificação de dados bronze, prata e ouro.

## Objetivo
O objetivo principal deste projeto é automatizar a extração, transformação e carregamento (ETL) de dados de plataformas de venda de componentes eletrônicos, permitindo uma análise eficiente e organizada dos dados coletados.

## Estrutura do Projeto

### 1. Extração de Dados (Bronze)
- **Descrição**: Extração de dados brutos das plataformas de venda utilizando Selenium.
- **Tecnologia**: Selenium, Python
- **DAGs**: `extract_bronze_data`

### 2. Transformação Inicial (Prata)
- **Descrição**: Limpeza e transformação inicial dos dados para padronização e consistência.
- **Tecnologia**: Apache Spark, Python
- **DAGs**: `transform_silver_data`

### 3. Transformação Avançada e Enriquecimento (Ouro)
- **Descrição**: Enriquecimento dos dados e preparação para análise avançada.
- **Tecnologia**: Apache Spark, Python
- **DAGs**: `transform_gold_data`

## Dependências
- **Apache Airflow**: Orquestração de workflows.
- **Selenium**: Extração de dados da web.
- **Apache Spark**: Processamento e transformação de dados.
- **Python**: Linguagem de programação principal.
