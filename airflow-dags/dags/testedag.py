from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 4, 30)
}

@dag(
    schedule_interval='*/2 * * * *',
    default_args=default_args,
    description='A DAG running tasks on Kubernetes every minute',
    tags=['python_kubernetes_workflow'],
    catchup=False,
    dag_id='python_kubernetes_workflow_v2'
)
def python_kubernetes_workflow():

    t2 = KubernetesPodOperator(
        namespace='airflow',
        image='python:3.7',
        image_pull_policy='Always',
        cmds=["python", "-c", "print('hello task 2 ..................')"],
        labels={"foo": "bar"},
        name="task-2",
        is_delete_operator_pod=True,
        in_cluster=False,
        task_id="task-2",
        config_file='/home/airflow/.kube/config',
        get_logs=True
    )

    t2

dag_instance = python_kubernetes_workflow()
