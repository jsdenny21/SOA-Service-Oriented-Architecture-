import time
from celery import Celery
from sqlalchemy import true

primeget = Celery('prime', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

primeget.conf.task_routes = {
    'prime.getprime': {'queue': 'prime'}
}

@primeget.task
def getprime(get):
    time.sleep(2) 
    temp = 0
    i=2
    while(temp<get):
        prime=True
        for k in range(2,i):
            if i%k==0:
                prime=False
        if prime:
            temp+=1
        if temp<get:
            i+=1
    return i        