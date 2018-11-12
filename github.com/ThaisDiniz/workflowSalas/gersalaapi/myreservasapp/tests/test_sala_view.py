from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from rest_framework import status

from myreservasapp.models import Sala
from myreservasapp.views import SalaList

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class TestSalaView(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='magalu10@')
        self.user.set_password('testethais')
        self.user.save()
        self.view = SalaList.as_view()

        token = Token.objects.get(user__username='magalu10@')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.data = {'nomeSala': 'star wars', 'idlocalidade': '1', 'qtdPessoasSentadas': '5',
                     'qtdLotacaomax': '08', 'flagRecursosVisuais':'1', 'flagPontoRede':'1'}


    def test_sala_view_success_status_code(self):
        url = reverse('api:salas', kwargs={'pk': self.Sala.pk})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.Sala.pk)
        self.assertEquals(response.status_code, 200)

    def test_sala_view_not_found_status_code(self):
        url = reverse('api:salas', kwargs={'pk': 99})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=99)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sala_view_failure_status_code(self):
        url = reverse('api:salas')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_sala_url_resolves_comment_view(self):
        view = resolve('/sala/1/')
        self.assertEquals(view.func.view_class, Sala)

    def test_sala_put_success_status_code(self):
        url = '/sala/{0}'.format(self.Sala.pk)
        request = self.client.put(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_sala_put_failure_data_error_status_code(self):
        url = '/sala/{0}'.format(self.Sala.pk)
        request = self.client.put(url)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sala_put_failure_status_code(self):
        url = '/sala/99'
        request = self.client.put(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_sala_delete_success_status_code(self):
        url = '/sala/{0}/'.format(self.Sala.pk)
        request = self.client.delete(url)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_sala_delete_failure_status_code(self):
        url = '/sala/99'
        request = self.client.delete(url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)
