# Generated by Django 4.0.3 on 2022-04-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyturismo', '0002_alter_destinoturistico_horario_viaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='idboleto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transporte',
            name='idtransporte',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]