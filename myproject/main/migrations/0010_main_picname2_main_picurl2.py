# Generated by Django 4.0.4 on 2022-04-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_main_picname_main_picurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl2',
            field=models.TextField(default=''),
        ),
    ]
