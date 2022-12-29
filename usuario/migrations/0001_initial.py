# Generated by Django 4.1.4 on 2022-12-29 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=7)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=50)),
                ('contato', models.CharField(max_length=11)),
                ('departamento', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=8)),
                ('confirm_senha', models.CharField(max_length=8)),
            ],
        ),
    ]
