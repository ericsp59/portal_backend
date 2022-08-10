from django.shortcuts import render
import os
import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser


# Create your views here.
def upload_func(name,file):
    with open(name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

class PortalFrontApiView(APIView):
    parser_classes = [FileUploadParser]
    def post(self, request):
        file_obj = request.data['file']
        name = request.data['file'].name
        # print(name)
        # f = file_obj.read().decode('utf-8')
        file = request.FILES.get('file')
        upload_func(name, file)
        list_files = subprocess.run(["D:/DISTR/utils/pscp/pscp.exe -i id_rsa", name, "root@172.16.16.21:/root/semaphore-operator/playbooks"], shell=True)
        list_files = subprocess.run(["ssh","root@172.16.16.21","-i id_rsa", "bash syncgit.sh"], shell=True)
        print("The exit code was: %d" % list_files.returncode)
        return Response({'post': 'ok', 'name': name})

        

    # def put(self, request):
    #     file_obj = request.data['file']
    #     print(file_obj.readable())
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(status=204)    
