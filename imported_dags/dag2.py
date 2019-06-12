from datetime import datetime, timedelta

# Functions to be converted into tasks
def printA():
    print("a")

def addThenPrint():
    a = 45
    b = 33
    print(a + b)

# The default arguments for this file's DAG
default_args = {
    'owner': 'dag1owner',
    'start_date': datetime(2014, 6, 3),
    'depends_on_past': False,
    'email': ['dags2@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

schedule_interval = timedelta(seconds=40)