# Generated by Django 2.1.5 on 2022-03-30 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220331_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='main',
            name='tel',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
