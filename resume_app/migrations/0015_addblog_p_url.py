# Generated by Django 3.2.3 on 2021-05-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0014_auto_20210529_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='p_url',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
    ]
