from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# add project path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pipeline.extract import extract_all
from pipeline.cleaning import clean_data
from pipeline.transform import transform
from pipeline.load import load_data
from database.db import save_to_db

default_args = {
    'owner' : 'office_admin',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=5)
}

def run_pipeline():
    att, tasks, sales = extract_all()
    att, tasks, sales = clean_data(att, tasks, sales)

    df = transform(att, tasks, sales)

    load_data(df)
    save_to_db(df)

    print("Pipeline executed successfully")

with DAG(
    dag_id = 'office_etl_pipeline'
    default_args = default_args,
    description = 'Office Daily ETL Pipeline',
    schedule_interval = '@daily',
    start_date = datetime(2026, 1, 1),
    catchup = False 
) as dag:
    run_etl = PythonOperator(
        task_id = 'run_pipeline',
        python_callable = run_pipeline
    )

    run_etl