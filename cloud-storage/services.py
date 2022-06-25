from MySQLdb import DatabaseError
from nameko.rpc import rpc

import database

class Service:

    name = 'services'

    database = database.Database()
    

    @rpc
    def regis(self,user,pas):
        users=self.database.regis(user,pas)
        return users

    @rpc
    def login(self,user,pas):
        users=self.database.login(user,pas)
        return users

    @rpc
    def upload(self,str,array1,array2):
        users=self.database.upload(str,array1,array2)
        return users

    @rpc
    def get_file(self,name,id):
        user=self.database.get_file(name,id)
        return user