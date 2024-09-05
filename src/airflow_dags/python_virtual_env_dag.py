from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
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


# Define a simple Python function
def print_hello():
    print("Hello, Airflow from a virtual environment!")


# Define the DAG with just one task with PythonVirtualenvOperator
with DAG(
    "simple_python_virtualenv_dag",
    default_args=default_args,
    description="A simple DAG with a PythonVirtualenvOperator",
    schedule_interval=timedelta(days=1),
) as dag:
    # Create a PythonVirtualenvOperator
    PythonVirtualenvOperator(
        task_id="hello_task",
        python_callable=print_hello,
        requirements=["requests"],  # Example requirement
        system_site_packages=False,
        dag=dag,
    )
