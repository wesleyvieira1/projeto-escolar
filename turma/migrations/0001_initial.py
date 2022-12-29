# Generated by Django 4.1.4 on 2022-12-29 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_turma', models.CharField(blank=True, max_length=50)),
                ('horario_inicio_turma', models.CharField(max_length=30)),
                ('horario_fim_turma', models.CharField(max_length=30)),
                ('etapa_turma', models.CharField(max_length=30)),
                ('dia_turma', models.CharField(max_length=30)),
                ('disciplina_turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplinas_turmas', to='disciplina.disciplina')),
            ],
        ),
    ]