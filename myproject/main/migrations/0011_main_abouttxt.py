# Generated by Django 4.0.4 on 2022-04-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_main_picname2_main_picurl2'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='abouttxt',
            field=models.TextField(default='-'),
        ),
    ]
