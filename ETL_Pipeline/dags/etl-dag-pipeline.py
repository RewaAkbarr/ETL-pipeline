from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "dibimbing",
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
    description="A complete data pipeline for transform and load using Spark",
    start_date=days_ago(1),
)

ETL_task = SparkSubmitOperator(
    application="/spark-scripts/transform.py",  # Path to your Spark script for transformation
    conn_id="spark_main",
    task_id="transform_data",
    dag=dag,
)

# Define task dependencies
ETL_task 