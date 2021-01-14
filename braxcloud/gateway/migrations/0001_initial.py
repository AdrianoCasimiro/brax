# Generated by Django 3.1.4 on 2021-01-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0002_auto_20201221_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('hostname', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.planta')),
            ],
        ),
    ]
