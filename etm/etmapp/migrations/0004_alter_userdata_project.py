# Generated by Django 3.2.5 on 2021-08-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etmapp', '0003_auto_20210818_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='project',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
