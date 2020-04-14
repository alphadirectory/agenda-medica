# Generated by Django 2.2.10 on 2020-04-13 04:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200412_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 4, 12, 3, 402406, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Horas'),
        ),
    ]