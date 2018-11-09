from django.conf.urls import url

from .CustomAuthToken import CustomAuthToken
from .views import token_request
from . import views

urlpatterns = [

     url(r'^api-token-auth/', CustomAuthToken.as_view()),

     url(r'^usuarios/$', views.UsuarioList.as_view(), name='usuario-list'),
     url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view(), name='usuario-detail'),

     url(r'^salas/$', views.SalaList.as_view(), name='sala-list'),
     url(r'^sala/(?P<pk>[0-9]+)/$', views.SalaDetail.as_view(), name='sala-detail'),

     url(r'^localidades/$', views.LocalidadeList.as_view(), name='localidade-list'),
     url(r'^localidade/(?P<pk>[0-9]+)/$', views.LocalidadeDetail.as_view(), name='localidade-detail'),

     url(r'^reservas/$', views.ReservaList.as_view(), name='reserva-list'),
     url(r'^reserva/(?P<pk>[0-9]+)/$', views.ReservaDetail.as_view(), name='reserva-detail'),

]
