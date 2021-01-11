# Generated by Django 3.1.4 on 2021-01-11 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sensor', '0005_auto_20201222_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertaTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora', models.DateTimeField()),
                ('valor', models.IntegerField()),
                ('checado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=5)),
                ('descricao_defeito', models.CharField(blank=True, max_length=200, null=True)),
                ('primeiro_aviso', models.BooleanField(default=False)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alertas', to='sensor.sensortemp')),
            ],
            options={
                'get_latest_by': ['datahora'],
            },
        ),
    ]
