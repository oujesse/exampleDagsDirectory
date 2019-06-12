from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import importlib

importedDagsPath = os.path.dirname(os.path.realpath(__file__)) + "/imported_dags"
default_args = {
    'owner': 'dags',
    'start_date': datetime(2015, 6, 10),
    'depends_on_past': True,
    'email': ['dags@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}
schedule_interval = timedelta(minutes=1)

# Loops through all python files in './imported_dags' and constructs dags out of them
for filename in os.listdir(importedDagsPath):
    if filename != "__pycache__" and filename != "__init__.py":
        # Imports the file as dagModel
        dagModel = importlib.import_module("imported_dags." + filename[:-3])
        if hasattr(dagModel, 'default_args'):
            current_default_args = dagModel.default_args
        else:
            current_default_args = default_args
        if hasattr(dagModel, 'schedule_interval'):
            current_schedule_interval = dagModel.schedule_interval
        else:
            current_schedule_interval = schedule_interval
        # Creates a global variable with variable name being filename[:-3] and the value being a DAG
        # Necessary for Airflow because dags/tasks are automatically constructed through global variables
        globals()[filename[:-3]] = DAG(filename[:-3], default_args=current_default_args, schedule_interval=current_schedule_interval)
        # Constructs the dag's corresponding tasks as global variables out of the file's python functions
        for key, val in dagModel.__dict__.items():
            if callable(val):
                globals()[key] = PythonOperator(
                    task_id=key,
                    python_callable=val,
                    dag=globals()[filename[:-3]]
                )
                # TODO: Implement dependencies
