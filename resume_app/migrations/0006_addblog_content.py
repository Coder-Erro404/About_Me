# Generated by Django 3.2.3 on 2021-05-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0005_rename_hotel_main_img_addblog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
