# Generated by Django 5.1 on 2024-09-02 18:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0003_alter_ocorrenciausuario_setor'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocorrenciausuario',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]