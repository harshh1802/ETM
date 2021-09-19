# Generated by Django 3.2.5 on 2021-08-22 17:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('etmapp', '0016_auto_20210819_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.date(2021, 8, 22)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 8, 22)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(default=datetime.date(2021, 8, 22)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_start',
            field=models.DateField(default=datetime.date(2021, 8, 22)),
        ),
        migrations.CreateModel(
            name='ExtdUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='NA', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
