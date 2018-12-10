"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^home/', views.home, name='home'),
	url(r'^contato/', views.contatos, name='contatos'),
	url(r'^detalhes/', views.Novidades_detalhes, name='detalhes'),
	url(r'^year/(?P<year>[0-9]{4})', views.Novidades_anual, name='novidades'),
	url(r'^registro/', views.registro, name='registro'),
    url(r'^admin/', admin.site.urls),
]