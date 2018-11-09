# Generated by Django 2.1.3 on 2018-11-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myreservasapp', '0011_auto_20181107_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localidade',
            name='ladoAndar',
        ),
        migrations.RemoveField(
            model_name='localidade',
            name='nomePredio',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='datahorareserva',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='flagPontoRede',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='flagRecursosVisuais',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='nomeSala',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='qtdlotacaoMax',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.AddField(
            model_name='localidade',
            name='ladoandar',
            field=models.CharField(blank=True, db_column='ladoAndar', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='localidade',
            name='nomepredio',
            field=models.CharField(blank=True, db_column='nomePredio', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='datareserva',
            field=models.DateField(blank=True, db_column='dataReserva', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='flagdiatodo',
            field=models.BooleanField(blank=True, db_column='flagdiatodo', null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='horario',
            field=models.TimeField(blank=True, db_column='horario', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='flagpontorede',
            field=models.BooleanField(blank=True, db_column='flagPontoRede', null=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='flagrecursosvisuais',
            field=models.BooleanField(blank=True, db_column='flagRecursosVisuais', null=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='nomesala',
            field=models.CharField(blank=True, db_column='nomeSala', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='qtdLotacaomax',
            field=models.TextField(blank=True, db_column='qtdLotacaomax', null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='descricaoemail',
            field=models.CharField(blank=True, db_column='descricaoEmail', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nomeusuario',
            field=models.CharField(blank=True, db_column='nomeUsuario', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numcelular',
            field=models.TextField(blank=True, db_column='numCelular', null=True),
        ),
        migrations.AlterField(
            model_name='localidade',
            name='andar',
            field=models.CharField(blank=True, db_column='andar', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sala',
            name='qtdPessoasSentadas',
            field=models.TextField(blank=True, db_column='qtdPessoasSentadas', null=True),
        ),
    ]
