# Generated by Django 3.2.3 on 2021-05-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0012_alter_addblog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addblog',
            old_name='Project_name',
            new_name='Title',
        ),
        migrations.RemoveField(
            model_name='addblog',
            name='P_content',
        ),
        migrations.AddField(
            model_name='addblog',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addblog',
            name='Decri',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='addblog',
            name='author',
            field=models.CharField(max_length=13),
        ),
    ]