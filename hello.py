from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define default_args dictionary to specify default parameters
default_args = {
    'owner': 'ananya',
    'start_date': datetime(2023, 11, 9),
    'retries': 1,
}

# Create a DAG object with the specified default arguments
dag = DAG('hello_dag', default_args=default_args, schedule_interval=None)

# Define the tasks
start_task = DummyOperator(task_id='start_task', dag=dag)

def say_hello():
    print("Hello, from Airflow!")

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=say_hello,
    dag=dag
)

end_task = DummyOperator(task_id='end_task', dag=dag)

# Define task dependencies
start_task >> hello_task >> end_task
