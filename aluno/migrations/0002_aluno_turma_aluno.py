# Generated by Django 4.1.1 on 2023-01-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0006_alter_turma_ano_turma_alter_turma_dia_turma_and_more'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='turma_aluno',
            field=models.ManyToManyField(to='turma.turma'),
        ),
    ]