# Generated by Django 2.1.5 on 2022-03-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='tel',
            field=models.TextField(default='-'),
        ),
    ]
