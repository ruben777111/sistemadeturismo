# Generated by Django 4.0.3 on 2022-04-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyturismo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinoturistico',
            name='horario_viaje',
            field=models.CharField(max_length=10, null=True, verbose_name='Horario'),
        ),
    ]
