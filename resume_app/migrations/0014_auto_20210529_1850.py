# Generated by Django 3.2.3 on 2021-05-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0013_auto_20210529_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addblog',
            old_name='Title',
            new_name='p_name',
        ),
        migrations.RemoveField(
            model_name='addblog',
            name='email',
        ),
        migrations.AlterField(
            model_name='addblog',
            name='author',
            field=models.CharField(max_length=225),
        ),
    ]
