# Generated by Django 5.1 on 2024-09-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computador',
            name='numero_nota_fiscal_computador',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='computador',
            name='numero_nota_fiscal_sistem_operacional',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='softwarecomputador',
            name='numero_nota_software',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
