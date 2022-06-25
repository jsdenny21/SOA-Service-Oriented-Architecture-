import time
from celery import Celery

palindrome = Celery('prime', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

palindrome.conf.task_routes = {
    'palindrom.checkpalindrome': {'queue': 'palindrome'}
}

def Palindrome(n):
    temp=n
    tot=0
    while(temp>0):
        temp1=temp%10
        temp=temp//10
        tot=tot*10+temp1
    if tot==n:
        return True
    else:
        return False

def Prime(n):
        if(n==1 | n==0):
            return False
        for i in range(2, n):
            if(n%i==0):
                return False
        return True

@palindrome.task
def checkpalindrome(get):
    time.sleep(1)
    count = 0
    i = 1
    while(count<=get):
        if(Prime(i) & Palindrome(i)):
            count = count + 1
        if count <= get:
            i = i + 1
    return i