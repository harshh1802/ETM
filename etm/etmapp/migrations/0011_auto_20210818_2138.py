# Generated by Django 3.2.5 on 2021-08-18 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etmapp', '0010_auto_20210818_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.date(2021, 8, 18)),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 8, 18)),
        ),
    ]
