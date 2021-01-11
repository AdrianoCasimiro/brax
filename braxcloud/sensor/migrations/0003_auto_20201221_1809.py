# Generated by Django 3.1.4 on 2020-12-21 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20201221_1729'),
        ('sensor', '0002_auto_20201221_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='planta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.planta'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='setor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.setor'),
        ),
    ]
