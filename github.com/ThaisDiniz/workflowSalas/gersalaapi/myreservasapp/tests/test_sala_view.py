from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from rest_framework import status

from myreservasapp.views import SalaList, SalaDetail

from rest_framework.test import APIRequestFactory


class TestSalaView(TestCase):
   
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='user_magalu')
        self.user.set_password('admin')
        self.user.save()
        self.view = SalaList.as_view()

        self.data = {'nomeSala': 'star wars', 'idlocalidade': '1', 'qtdPessoasSentadas': '5',
                     'qtdLotacaomax': '08', 'flagRecursosVisuais':'1', 'flagPontoRede':'1'}

    def test_sala_view_failure_status_code(self):
        url = resolve('/salas/')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_sala_url_resolves_comment_view(self):
        view = resolve('/sala/1/')
        self.assertEquals(view.func.view_class, SalaDetail)