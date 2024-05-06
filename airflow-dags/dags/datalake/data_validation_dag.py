from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator

import pandas as pd
import requests
import json

default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 4, 30)
}

@dag(
    schedule_interval='1 * * * *',
    default_args=default_args,
    description='A simple data validation DAG using Airflow 2.9.0 features',
    tags=['data_validation', 'example'],
    catchup=False,
    dag_id='data_validation_dag_v2'
)
def data_validation_dag_v2():
    @task
    def fetch_data():
        """Fetch data from an API and convert to DataFrame."""
        url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
        response = requests.get(url)
        return pd.DataFrame(json.loads(response.text))

    @task
    def count_records(df: pd.DataFrame) -> int:
        """Return the number of records in the DataFrame."""
        return len(df.index)

    @task
    def validate_records(record_count: int) -> str:
        """Determine the next step based on record count."""
        if record_count > 1000:
            print('Record count is valid.')
        else:
            print('Record count is invalid.')

    # Start and end operators are using EmptyOperator which is functionally similar to DummyOperator
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    df = fetch_data()
    record_count = count_records(df)
    validate_records(record_count)

    start >> df >> record_count >> validate_records(record_count) >> end

dag_instance = data_validation_dag_v2()
