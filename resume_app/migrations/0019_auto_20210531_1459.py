# Generated by Django 3.2.3 on 2021-05-31 09:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0018_addblog_content1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addblog',
            name='content1',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='p_url',
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
