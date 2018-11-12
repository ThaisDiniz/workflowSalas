from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from rest_framework import status

from myreservasapp.views import ReservaList, ReservaDetail

from rest_framework.test import APIRequestFactory


class TestReservaView(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='magalu10@')
        self.user.set_password('testethais')
        self.user.save()
        self.view = ReservaList.as_view()

        self.data = {'idreserva': '1', 'idUsuario': '1', 'dataReserva': '2018-11-12'
                    ,'tituloReserva':'reuniao','horaReserva': '08:00',  'flagDiaTodo':'1'}

    def test_reserva_view_failure_status_code(self):
        url = resolve('/reservas/')
        request = self.factory.get(url)
        response = self.view(request)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_reserva_url_resolves_comment_view(self):
        view = resolve('/reserva/1/')
        self.assertEquals(view.func.view_class, ReservaDetail)