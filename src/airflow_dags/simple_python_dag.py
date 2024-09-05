from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def print_hello():
    print("Hello, Airflow!")


# Define the DAG
with DAG(
    "simple_python_dag",
    default_args=default_args,
    description="A simple DAG with a Python operator",
    schedule_interval=timedelta(days=1),
) as dag:
    bash_task = BashOperator(
        task_id="print_date",
        bash_command="date",
    )
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_hello,
        dag=dag,
    )

    bash_task >> hello_task
