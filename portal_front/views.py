from django.shortcuts import render
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
        print(name)
        # f = file_obj.read().decode('utf-8')
        file = request.FILES.get('file')
        upload_func(name, file)
        return Response({'post': 'ok'})

        

    # def put(self, request):
    #     file_obj = request.data['file']
    #     print(file_obj.readable())
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(status=204)    
