# Generated by Django 4.0.4 on 2022-04-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_body_txt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_txt',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
