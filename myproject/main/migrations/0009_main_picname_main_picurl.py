# Generated by Django 4.0.4 on 2022-04-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_main_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl',
            field=models.TextField(default=''),
        ),
    ]
