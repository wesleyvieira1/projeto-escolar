# Generated by Django 4.1.4 on 2023-01-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='img_user',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='img_user',
            field=models.ImageField(blank=True, null=True, upload_to='usuario_profile'),
        ),
    ]
