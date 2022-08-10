import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .models import PortalFrontSettings


# Create your views here.
def upload_func(name,file):
    with open(name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

class PortalFrontApiView(APIView):
    parser_classes = [FileUploadParser]
    def post(self, request):
        settings = PortalFrontSettings.objects.get(pk=1)
        print(settings.semaphore_srv_address)

        name = request.data['file'].name

        file = request.FILES.get('file')
        upload_func(name, file)
        command = subprocess.run([f'{settings.copy_files_program} -i {settings.semaphore_srv_priv_key_file}', name, f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}:/{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir}/playbooks'], shell=True)
        command = subprocess.run(["ssh",f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}',f'-i {settings.semaphore_srv_priv_key_file}', "bash syncgit.sh"], shell=True)
        print("The exit code was: %d" % command.returncode)
        return Response({'post': 'ok', 'name': name})

        

    # def put(self, request):
    #     file_obj = request.data['file']
    #     print(file_obj.readable())
    #     # ...
    #     # do some stuff with uploaded file
    #     # ...
    #     return Response(status=204)    
