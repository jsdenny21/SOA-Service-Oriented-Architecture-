from nameko.rpc import rpc
import time
# import palindrom
from prime import getprime , primeget
from palindrom import checkpalindrome , palindrome
from celery.result import AsyncResult

class prime:
    name = "primeservice"

    
    @rpc
    def prime(self, num):
        id = getprime.apply_async([num])
        result = AsyncResult(id.id, app=primeget)
        return result.get()
    
    @rpc
    def palindrome(self, num):
        id = checkpalindrome.apply_async([num])
        result = AsyncResult(id.id, app=palindrome)
        return result.get()
        