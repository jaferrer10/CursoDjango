# Generated by Django 2.2.6 on 2020-03-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0006_auto_20200309_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion Web'),
        ),
    ]