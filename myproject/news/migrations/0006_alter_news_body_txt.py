# Generated by Django 4.0.4 on 2022-04-13 10:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_txt',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]