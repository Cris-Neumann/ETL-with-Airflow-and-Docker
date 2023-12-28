# Script que se ejecuta cada 1 minuto en Apache Airflow, el cual abre un archivo CSV,
# actualizando y/o insertando regitros en BBDD PostgreSQL.
import subprocess
from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

args_por_defecto = {'owner': 'owner_de_prueba', 'start_date': datetime(2023, 7, 6, 22, 50, 0)}

with DAG(dag_id='ETL_dag', default_args=args_por_defecto, schedule_interval='*/1 * * * *') as dag:
    start_task = EmptyOperator(task_id='start')
    etl_task = BashOperator(task_id='id_etl_task', bash_command='python /opt/airflow/ETL_scripts/ETL.py')
    end_task = EmptyOperator(task_id='end')
start_task >> etl_task >> end_task
