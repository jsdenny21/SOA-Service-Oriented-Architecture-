import json
from matplotlib.font_manager import json_dump

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
                if session['Username']==name and session['Password']==pas:
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
        if not os.path.exists('file'):
            os.mkdir('file')
        cookies=request.cookies.get('SESSID')

        if cookies != None:
            if 'news' not in request.files:
                return 'Key not insert'
            
            news=request.files.getlist('news')
            for i in news:
                if i.filename =='':
                    return 'FILE NOT INSERT YET'
            

            session =self.session_provider.get_session(cookies)
            path=[]
            newsarray=[]
            for news1 in news:
                app = Flask(__name__)
                app.config['upload']='file'
                filename = secure_filename(news1.filename)
                news1.save(os.path.join(app.config['upload'],filename))
                # name = filename.split('.')[-1]
                newsarray.append(news1)
                temp='file/'+news1
                path.append(temp) 

            upload=self.user_rpc.upload(session['Username'],newsarray,path)
            return upload

        else:
            return 'MUST LOGIN'

    #download
    @http('GET','/download/<int:id>')
    def download(self,request,id):
        cookies=request.cookies.get('SESSID')

        if cookies != None:
            session =self.session_provider.get_session(cookies)

            file=self.user_rpc.get_file(session['Username'],id)

            # return json.dumps(file)
            if file['status'] == 'not':
                return json.dumps(file['Messsage'])
            response = Response(open(file['path'], 'rb').read())
            file_type = file['file'].split('.')[-1]
            
            response.headers['Content-Type'] = EXTENSION_HEADER[file_type]
            response.headers['Content-Disposition'] = 'attachment; filename={}'.format(file['file'])
            
            return response
        else:
            return 'MUST LOGIN'
        




