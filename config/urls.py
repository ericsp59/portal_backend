"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from crm import views
from portal_app.views import portal_app

from portal_logs.views import PortalLogsApiView
from portal_front.views import  PortalFrontApiView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    path('form_response/', views.form_response, name='form_response'),
    path('portal/', portal_app, name='portal_app'),
    path('api/v1/log_list/', PortalLogsApiView.as_view()),
    path('api/v1/add_playbook/', PortalFrontApiView.as_view()),
    path('api/v1/', include('portal_front.urls'))

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)