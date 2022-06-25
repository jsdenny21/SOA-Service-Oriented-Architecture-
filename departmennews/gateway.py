import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http
from rediss import SessionProvider
from werkzeug.wrappers import Response
import uuid

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from unittest import result
from grpc import Status

EXTENSION_HEADER = {
    'txt': 'text/plain',
    'pdf': 'application/pdf',
    'docx': 'application/docx',
    'png': 'image/png',
    'ico':'image/icon',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif'
}
class GatewayService:
    name = 'gateway'

    user_rpc = RpcProxy('services')
    session_provider = SessionProvider()

    @http('GET', '/user/<string:str>')
    def checkUser(self, request,str):
        rooms = self.user_rpc.checkUser(str)
        return rooms

    #regis
    @http('POST', '/regis')
    def regis(self, request):
        req=request.json
        name=req["Username"]
        pas=req["Password"]
        reg = self.user_rpc.regis(name,pas)
        return reg

    #login
    @http('GET', '/login')
    def login(self, request):
        req=request.json
        name=req["Username"]
        pas=req["Password"]
        reg = self.user_rpc.login(name,pas)
        # return reg
        if reg == 1:
            cookies = request.cookies.get('SESSID')
           
            users={
                    'Username':name,
                    'Password':pas
                }
            if cookies==None:
                sessionID=self.session_provider.set_session(users)
                response = Response(str(users))
                response.set_cookie('SESSID',sessionID)
                return response
                
            else:
                session =self.session_provider.get_session(cookies)
                if session['Username']==name:
                    return "Already Login"
                else:
                    session=self.session_provider.set_session(users)
                    response=Response(str(users))
                    response.set_cookie('SESSID',sessionID)
                return response
            # return str(reg)
        else:
            return "Username not Found!"



    #logout
    @http('GET','/logout')
    def logout(self,request):
        cookies=request.cookies
        if cookies:
            check = self.session_provider.del_session(cookies['SESSID'])
            response = Response(cookies['SESSID'])
            response.delete_cookie('SESSID')
            return response
        else:
            return "Not login yet!"

    #UPLOAD
    @http('POST','/file')
    def upload(self,request):
        if not os.path.exists('news'):
            os.mkdir('news')
        cookies=request.cookies.get('SESSID')
        if cookies != None:
            if 'news' not in request.files:
                return 'Key not insert'
            
            news=request.files.getlist('news')
            for i in news:
                if i.filename =='':
                    return 'FILE NOT INSERT YET'
            
            path=[]
            newsarray=[]
            for news1 in news:
                app = Flask(__name__)
                app.config['upload']='news'
                filename = secure_filename(news1.filename)
                news1.save(os.path.join(app.config['upload'],filename))
                newsarray.append(filename)
                temp='news/'+filename
                path.append(temp) 

            upload=self.user_rpc.upload(newsarray,path)
            return upload

        else:
            return 'MUST LOGIN'


    #view
    @http('GET','/allnews')
    def view(self,request):
        get=self.user_rpc.allnews()
        return json.dumps(get,indent=4)
    
    #view id
    @http('GET','/news/<int:file_id>')
    def view_by_id(self,request,file_id):
        session=request.cookies.get('SESSID')
        if session != None:
            get=self.user_rpc.newsbyid(file_id)


            return json.dumps(get,indent=4)
        else:
            return "MUST LOGIN"

    #update/deleted 
    @http('PUT','/deleted/<int:file_id>')
    def deleted(self,request,file_id):
        session=request.cookies.get('SESSID')
        if session != None:
            get=self.user_rpc.deleted(file_id)
            return json.dumps(get,indent=4)
        else:
            return "MUST LOGIN"
    
    @http('PUT','/edit/<int:file_id>')
    def edit(self,request,file_id):
        session=request.cookies.get('SESSID')
        req=request.json
        name=req['new_name']
        if session != None:
            get=self.user_rpc.edit(file_id,name)
            return json.dumps(get,indent=4)
        else:
            return "MUST LOGIN"

    @http('GET','/download/<int:id>')
    def download(self,request,id):
        file = self.user_rpc.get_file(id)
        if file['status'] == 'not':
            return {
                'message':'id not found'
            }
        
        response = Response(open(file['path'], 'rb').read())
        file_type = file['news'].split('.')[-1]
        
        response.headers['Content-Type'] = EXTENSION_HEADER[file_type]
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(file['news'])
        
        return response

    #UPLOAD test
    @http('POST','/file/testing')
    def upload1(self,request):
        if not os.path.exists('news'):
            os.mkdir('news')

        if 'news' not in request.files:
            return 'Key not insert'
        
        news=request.files.getlist('news')
        for i in news:
            if i.filename =='':
                return 'FILE NOT INSERT YET'
        
        path=[]
        temp=''
        newsarray=[]
        for news1 in news:
            app = Flask(__name__)
            app.config['upload']='news'
            filename = secure_filename(news1.filename)
            news1.save(os.path.join(app.config['upload'],filename))
            newsarray.append(filename)
            temp='news/'+filename
            path.append(temp) 

        # upload=self.user_rpc.upload(newsarray,path)
        return temp

    #TEST test
    @http('POST','/TEST')
    def test(self,request):
        p=[]
        p=[1,2,3,4]
        return json.dumps(len(p))
    


