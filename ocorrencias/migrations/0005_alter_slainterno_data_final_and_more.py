# Generated by Django 5.1 on 2024-12-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocorrencias', '0004_slainterno_hora_final_slainterno_hora_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slainterno',
            name='data_final',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='slainterno',
            name='data_inicial',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='slainterno',
            name='hora_final',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='slainterno',
            name='hora_inicial',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='slainterno',
            name='ocorrido',
            field=models.TextField(),
        ),
    ]
