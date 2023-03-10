# Generated by Django 4.1.1 on 2023-01-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_alter_aluno_raca_aluno_alter_aluno_sexo_aluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sexo_aluno',
            field=models.CharField(choices=[('', 'Defina o sexo'), ('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro')], max_length=50),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turno_aluno',
            field=models.CharField(choices=[('', 'Defina o turno'), ('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Integral', 'Integral')], max_length=50),
        ),
    ]
