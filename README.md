# workflowSalas
API para controlar agendamentos de salas de reunião


Olá MagaBoys and MagaGirls, visto que a vaga é python, envio para vocês minha api construída em python tbm!!


$ para iniciar o serviço

python manage.py makemigrations


python manage.py migrate


python manage.py createsuperuser (usuario: user_magalu, email: teste@teste.com e senha: admin)


python manage.py runserver


$ para verificar usuário de autenticação

Django admin: 
http://127.0.0.1:8000/admin/


user_magalu


admin



● Uma API para criar
http://127.0.0.1:8000/reservas/

editar e remover agendamentos
http://127.0.0.1:8000/reserva/{id}

● Uma API para listar e filtrar agendamentos por data e sala


Obter sala reservada por filtro especifico


http://127.0.0.1:8000/reservas/?idSala=&idUsuario=&datareserva=2018-10-30&tituloreserva=&horario=&flagdiatodo=


http://127.0.0.1:8000/reservas/?idSala=&idUsuario=2&datareserva=&tituloreserva=&horario=&flagdiatodo=


● Uma API para criar, editar e remover salas de reuniões


Obter Sala por filtro


http://127.0.0.1:8000/salas/?nomesala=&idlocalidade=&qtdPessoasSentadas=5&qtdLotacaomax=&flagrecursosvisuais=&flagpontorede=


