# Generated by Django 4.2.7 on 2023-11-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_agencia_bancaria_mapeamento_agencia_bancaria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapeamento',
            name='id_tipo',
            field=models.CharField(max_length=200),
        ),
    ]