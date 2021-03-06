# Generated by Django 3.1.4 on 2020-12-22 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0003_auto_20201221_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'sensor', 'verbose_name_plural': 'sensores'},
        ),
        migrations.CreateModel(
            name='SensorTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora', models.DateTimeField()),
                ('t', models.FloatField(blank=True, default=0, null=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.sensor')),
            ],
            options={
                'get_latest_by': ['datahora'],
            },
        ),
        migrations.CreateModel(
            name='SensorDPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora', models.DateTimeField()),
                ('t', models.FloatField(blank=True, default=0, null=True)),
                ('h', models.FloatField(blank=True, default=0, null=True)),
                ('f60', models.FloatField(blank=True, max_length=10, null=True)),
                ('mcnt', models.FloatField(blank=True, max_length=10, null=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.sensor')),
            ],
            options={
                'get_latest_by': ['datahora'],
            },
        ),
    ]
