# Generated by Django 4.1.1 on 2023-01-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_aluno_turma_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='raca_aluno',
            field=models.CharField(choices=[('', 'Defina a raça'), ('Branca', 'Branca'), ('Preta', 'Preta'), ('Parda', 'Parda'), ('ND', 'Não declarada')], max_length=50),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sexo_aluno',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], max_length=50),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turno_aluno',
            field=models.CharField(choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Integral', 'Integral')], max_length=50),
        ),
    ]
