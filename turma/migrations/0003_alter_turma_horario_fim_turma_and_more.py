# Generated by Django 4.1.4 on 2023-01-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0002_remove_turma_aluno_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='horario_fim_turma',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='turma',
            name='horario_inicio_turma',
            field=models.TimeField(),
        ),
    ]
