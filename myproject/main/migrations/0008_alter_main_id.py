# Generated by Django 4.0.4 on 2022-04-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220331_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]