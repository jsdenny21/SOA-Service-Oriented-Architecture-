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
        sql = "SELECT count(*) as x FROM user where Username=%s"
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
        a=self.archive()
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT count(*) as x FROM user where Username=%s and Password=%s"
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
        a=self.archive()
        cursor = self.connection.cursor(dictionary=True)
        check = self.checkUser(user)
        if check == 0:
            sql="INSERT INTO `user`(`id`, `Username`, `Password`) VALUES (null,%s,%s)"
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

    def allnews(self):
        a=self.archive()
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from news"
        cursor.execute(sql)
        result=[]
        result.append({"status 0":"ready","status 1":"deleted","status 2":"archive"})
        for row in cursor.fetchall():
            result.append({
                "name news":row['name_news'],
                "status":row['deleted'],
                "date":row['length']
            })
        return result

    def newsbyid(self,id):
        a=self.archive()
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from news WHERE id=%s"
        cursor.execute(sql,[int(id)])
        row = cursor.fetchone()
        if cursor.rowcount > 0:
            result=[]
            result.append({"status 0":"ready","status 1":"deleted","status 2":"archive"})
            for row in cursor.fetchall():
                result.append({
                    "name news":row['name_news'],
                    "status":row['deleted'],
                    "date":row['length']
                })
            return result
        else:
            return {
                'Messsage':'id not found'
            }

    def deleted(self,id):
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from news WHERE id=%s"
        cursor.execute(sql,[int(id)])
        row=cursor.fetchone()
        if cursor.rowcount >0:
            
            if row['deleted'] != 1:
                a=self.archive()
                sql="UPDATE `news` SET `deleted`=%s WHERE id=%s"
                cursor.execute(sql,[int(1),int(id)])
                self.connection.commit()
                sql="SELECT * from news WHERE id=%s"
                cursor.execute(sql,[int(id)])
                result=[]
                result.append({"status 0":"ready","status 1":"deleted","status 2":"archive"})
                for row in cursor.fetchall():
                    result.append({
                        "name news":row['name_news'],
                        "status":row['deleted'],
                        "date":row['length']
                    })
                return result
            else:
                return {"message":"Already deleted"}
        else:
            return {"Error":"file not found!"}

    def edit(self,file_id,name):
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from news WHERE id=%s"
        cursor.execute(sql,[int(file_id)])
        row=cursor.fetchone()
        if cursor.rowcount >0:
            
            if row['deleted'] == 0:
                a=self.archive()
                sql="UPDATE `news` SET `name_news`=%s WHERE id=%s"
                cursor.execute(sql,[name,int(file_id)])
                self.connection.commit()
                sql="SELECT * from news WHERE id=%s"
                cursor.execute(sql,[int(file_id)])
                result=[]
                result.append({"status 0":"ready","status 1":"deleted","status 2":"archive"})
                for row in cursor.fetchall():
                    result.append({
                        "name news":row['name_news'],
                        "status":row['deleted'],
                        "date":row['length']
                    })
                return result
            elif  row['deleted'] != 2:
                return {"message":"Already archive"}
            else:
                return {"message":"Already deleted"}
        else:
            return {"Error":"file not found!"}
        
    def archive(self):
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from news t WHERE t.length < DATE_SUB(CURRENT_DATE,INTERVAL 1 MONTH)"
        cursor.execute(sql)
        row=cursor.fetchall()
        for i in row:
            if i['deleted'] !=1:
                sql="UPDATE `news` SET `deleted`=%s WHERE id=%s"
                cursor.execute(sql,[int(2),int(i['id'])])
                self.connection.commit()

        return 0

    def upload(self,newsarr,patharr):
        a=self.archive()
        cursor = self.connection.cursor(dictionary=True)

        length = len(patharr)
        i=0
        for news in newsarr:   
            sql = "INSERT INTO `news`(`id`, `name_news`, `path`, `deleted`, `length`) VALUES (null,%s,%s,%s,CURRENT_DATE())"
            cursor.execute(sql,[news,patharr[i],int(0)])
            i+=1
            self.connection.commit()        
        cursor.close()
        return 'upload succesfully'

    def get_file(self,id):
        a=self.archive()
        cursor = self.connection.cursor(dictionary=True)
        sql="SELECT * from news WHERE id=%s"
        cursor.execute(sql,[int(id)])
        row = cursor.fetchone()
        if cursor.rowcount > 0:
            result={'status':'get','news':row['name_news'],'path':row['path']}
            return result
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
    
    
# class SessionWrapper:
    
#     def __init__(self, connection):
#         # Redis Connection
#         self.redis = connection

#         # 1 Hour Expire (in Second)
#         self.default_expire = 60 * 60
    
#     def generate_session_id(self):
#         key = str(uuid.uuid4())
#         # while self.redis.exist(key):
#             # key = str(uuid.uuid4())
#         return key

#     def set_session(self, user_data):
#         # Pickle User Data so that can be stored in Redis
#         user_data_pickled = pickle.dumps(user_data)

#         # Get Session ID
#         session_id = self.generate_session_id()

#         # Store Session Data with Expire Time in Redis
#         self.redis.set(session_id, user_data_pickled, ex=self.default_expire)

#         return session_id
    
#     def get_session(self, session_id):
#         # Get the Data from Redis
#         result = self.redis.get(session_id)

#         if result:
#         # Unpack the user data from Redis
#             user_data = pickle.loads(result)
#         else:
#             user_data = None

#         return user_data

#     def del_session(self, session_id):
#         result = self.redis.delete(session_id)

#         return "BEGONE"
    
# class SessionProvider(DependencyProvider):

#     def setup(self):
#         self.client = redis.Redis(host='127.0.0.1', port=6379, db=0)
    
#     def get_dependency(self, worker_ctx):
#         return SessionWrapper(self.client)
    



