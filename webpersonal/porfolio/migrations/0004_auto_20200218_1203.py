# Generated by Django 2.1.7 on 2020-02-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0003_auto_20200218_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
