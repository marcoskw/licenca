# Generated by Django 5.1 on 2024-09-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0002_computador_numero_nota_fiscal_computador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwarecomputador',
            name='serial',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
