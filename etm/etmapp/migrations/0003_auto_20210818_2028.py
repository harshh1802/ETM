# Generated by Django 3.2.5 on 2021-08-18 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('etmapp', '0002_role_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
