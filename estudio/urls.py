from django.urls import  path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import  static

urlpatterns = [
    path("login/", views.login_request, name="login"),
    path('', views.login_request, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('index', views.index, name='index'),

    path('clientes', views.clientes, name='clientes'),
    path('clientes/crearC', views.crearC, name='crearC'),
    path('clientes/editarC', views.editarC, name='editarC'),
    path('eliminar/<int:idCli>', views.eliminarC, name='eliminarC'),
    path('clientes/editarC/<int:id>', views.editarC, name='editarC'),
    path('inactivosC/',views.inactivosC, name='inactivosC'),
    path('inactivosC/activarC/<int:idCli>', views.activarC, name='activarC'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)