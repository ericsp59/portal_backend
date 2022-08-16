import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import PortalFrontSettings
#from django.http import JsonResponse

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import NoteSerializer
from .models import Note


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
        # D:/DISTR/utils/pscp/pscp.exe
        # command = subprocess.run([f'{settings.copy_files_program}', f'/{name}', f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}:/{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir}/playbooks'])
        command = subprocess.run([f'{settings.copy_files_program} -i {settings.semaphore_srv_priv_key_file}', name, f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}:/{settings.semaphore_srv_user}/{settings.semaphore_srv_operator_dir}/playbooks'], shell=True)
        # command = subprocess.run(["ssh",f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}',f'-i {settings.semaphore_srv_priv_key_file}', "bash syncgit.sh"])
        command = subprocess.run(["ssh",f'{settings.semaphore_srv_user}@{settings.semaphore_srv_address}',f'-i {settings.semaphore_srv_priv_key_file}', "bash syncgit.sh"], shell=True)
        print("The exit code was: %d" % command.returncode)
        return Response({'post': 'ok', 'name': name})
     

    @api_view(['GET'])
    def getRoutes(request):
        routes = [
            '/api/token',
            '/api/token/refresh',
        ]
        return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    # notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
