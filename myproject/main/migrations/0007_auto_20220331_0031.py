# Generated by Django 2.1.5 on 2022-03-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220331_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
