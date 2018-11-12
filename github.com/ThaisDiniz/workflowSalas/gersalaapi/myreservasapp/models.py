from django.db import models


# Create your models here.
class Localidade(models.Model):

    class Meta:

        db_table = 'localidade'

    nomepredio = models.CharField(db_column='nomePredio', max_length=60, blank=True, null=True)  # Field name made lowercase.
    andar= models.CharField(db_column='andar', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ladoandar = models.CharField(db_column='ladoAndar', max_length=20, blank=True, null=True)  # Field name made lowercase.



class Usuario(models.Model):

    class Meta:

        db_table = 'usuario'

    nomeusuario = models.CharField(db_column='nomeUsuario', max_length=80, blank=True, null=True)  # Field name made lowercase.
    descricaoemail = models.CharField(db_column='descricaoEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numcelular = models.TextField(db_column='numCelular', blank=True, null=True)  # Field name made lowercase. This field type is a guess.


    @property
    def __str__(self):
        return self.nome,self.email,self.celular


class Sala(models.Model):

    class Meta:

        db_table = 'sala'

    nomesala = models.CharField(db_column='nomeSala', max_length=80, blank=True, null=True)  # Field name made lowercase.
    idlocalidade = models.IntegerField(db_column='idlocalidade')
    qtdPessoasSentadas = models.TextField(db_column='qtdPessoasSentadas', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'. This field type is a guess.
    qtdLotacaomax = models.TextField(db_column='qtdLotacaomax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    flagrecursosvisuais = models.BooleanField(db_column='flagRecursosVisuais', blank=True, null=True)  # Field name made lowercase.
    flagpontorede = models.BooleanField(db_column='flagPontoRede', blank=True, null=True)  # Field name made lowercase.



    @property
    def __str__(self):
        return self.nomeSala,self.qtdPessoasSentadas,self.qtdlotacaoMax,\
               self.flagRecursosVisuais,self.flagPontoRede



class Reserva(models.Model):

    class Meta:
        db_table='reserva'

    idSala =models.IntegerField()
    idUsuario = models.IntegerField()
    datareserva = models.DateField(db_column='dataReserva', unique=True, blank=True, null=True)  # Field name made lowercase.
    tituloreserva = models.CharField(db_column='tituloReserva', max_length=60, blank=True, null=True)  # Field name made lowercase.
    horario = models.TimeField(db_column='horario', unique=True, blank=True, null=True)  # Field name made lowercase.
    flagdiatodo = models.BooleanField(db_column='flagdiatodo', blank=True, null=True)  # Field name made lowercase.

    @property
    def __str__(self):
        return self.datahorareserva, self.tituloreserva


