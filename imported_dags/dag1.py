from datetime import datetime, timedelta

# Functions to be converted into tasks
def printHello():
    print("hello")

def printBye():
    print("bye")

def printGreetings():
    print("greetings")

# The default arguments for this file's DAG
default_args = {
    'owner': 'dag1owner',
    'start_date': datetime(2016, 6, 10),
    'depends_on_past': True,
    'email': ['dags1@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

schedule_interval = timedelta(seconds=30)