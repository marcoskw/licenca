# Generated by Django 5.1 on 2024-09-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametrosempresa',
            name='nome_exibicao',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]