from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)
from kubernetes.client.models import V1ResourceRequirements
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

# Define the DAG
with DAG(
    "simple_k8s_dag",
    default_args=default_args,
    description="A simple DAG with a KubernetesPodOperator",
    schedule_interval=timedelta(days=1),
) as dag:
    KubernetesPodOperator(
        task_id="echo",
        name="echo",
        namespace="default",
        image="alpine", # Use images available in DockerHub or private registry
        cmds=["echo"],
        arguments=["Hello, Kubernetes!"],
        container_resources=V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "128Mi"},
            limits={"cpu": "200m", "memory": "256Mi"},
        ),
        container_security_context=V1SecurityContext(read_only_root_filesystem=True),
    )
