from django.shortcuts import render

# Create your views here.

def portal_app(request):
    return render(request, './portal/index.html')
