# Generated by Django 5.1 on 2024-08-16 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0003_rename_licençasoftware_licencasoftware_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 16, 12, 35, 21, 521166, tzinfo=datetime.timezone.utc)),
        ),
    ]