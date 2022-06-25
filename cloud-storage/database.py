from nameko.extensions import DependencyProvider

import mysql.connector
import json
from mysql.connector import Error
from mysql.connector import pooling
import pickle
import uuid
import redis


class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        self.connection = connection
    
    def checkUser(self,str):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT count(*) as x FROM cloud_storage where Username=%s"
        cursor.execute(sql,[str])
        result = cursor.fetchone()
        check=0
        if result['x'] >0:
            check=1
        else:
            check=0
        cursor.close()
        return check

    #login
    def login(self,name,pas):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT count(*) as x FROM cloud_storage where Username=%s and Password=%s"
        cursor.execute(sql,[name,pas])
        result = cursor.fetchone()
        check=0
        if result['x'] >0:
            check=1
        else:
            check=0
        cursor.close()
        return check

    #regis
    def regis(self,user,pas):
        cursor = self.connection.cursor(dictionary=True)
        check = self.checkUser(user)
        if check == 0:
            sql="INSERT INTO `cloud_storage`(`id`, `Username`, `Password`) VALUES (null,%s,%s)"
            cursor.execute(sql,[user,pas])
            self.connection.commit()
            lis = self.checkUser(user)
            cursor.close()
            st=""
            if lis==1:
                st = user +"  "+pas+" registered"
            else:
                st = "Failed to registered"
            return st
        else:
            return "Username occupied"

    def upload(self,str,newsarr,patharr):
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from cloud_storage WHERE Username=%s"
        cursor.execute(sql,[str])
        row= cursor.fetchone()

        length = len(patharr)
        i=0
        for news in newsarr:   
            sql = "INSERT INTO `file`(`id`, `file`, `file_path`, `id_user`) VALUES (null,%s,%s,%s)"
            cursor.execute(sql,[news,patharr[i],row['id']])
            i+=1
            self.connection.commit()        
        cursor.close()
        return 'upload succesfully'

    def get_file(self,str,id):
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from cloud_storage WHERE Username=%s"
        cursor.execute(sql,[str])
        row = cursor.fetchone()

        sql="SELECT * from file WHERE id=%s"
        cursor.execute(sql,[id])
        file = cursor.fetchone()

        # return {
        #     'row':row['id'],'file':file['id_user']
        # }

        if cursor.rowcount > 0:
            if int(file['id_user']) == row['id']:
                result={'status':'get','file':file['file'],'path':file['file_path']}
                return result
            else:
                return {'status':'not',
                'Messsage':'USER NOT SAME'
            }
        else:
            return {'status':'not',
                'Messsage':'id not found'
            }
    
        

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=5,
                pool_reset_session=True,
                host='localhost',
                database='soa_news',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    
    



