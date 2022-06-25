from MySQLdb import DatabaseError
from nameko.rpc import rpc

import database

class Service:

    name = 'services'

    database = database.Database()
    
    @rpc
    def checkUser(self,str):
        rooms = self.database.checkUser(str)
        return rooms

    @rpc
    def regis(self,user,pas):
        users=self.database.regis(user,pas)
        return users

    @rpc
    def login(self,user,pas):
        users=self.database.login(user,pas)
        return users

    @rpc
    def upload(self,array1,array2):
        users=self.database.upload(array1,array2)
        return users

    @rpc
    def allnews(self):
        users=self.database.allnews()
        return users

    @rpc
    def newsbyid(self,inn):
        users=self.database.newsbyid(inn)
        return users
    
    @rpc
    def deleted(self,inn):
        users=self.database.deleted(inn)
        return users
    
    @rpc
    def edit(self,file_id,name):
        users=self.database.edit(file_id,name)
        return users
    
    @rpc
    def get_file(self,id):
        user=self.database.get_file(id)
        return user