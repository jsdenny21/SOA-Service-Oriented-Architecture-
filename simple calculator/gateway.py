import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayPrime:
    name = 'gatewayprime'

    prime_rpc = RpcProxy('primeservice')

    @http('GET', '/prime/<int:num>')
    def prime(self, request, num):
        result = self.prime_rpc.prime(num)
        return json.dumps(result)

    @http('GET', '/prime/palindrome/<int:num>')
    def palindrome(self, request, num):
        result = self.prime_rpc.palindrome(num)
        return json.dumps(result)
