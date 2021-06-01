# Generated by Django 3.2.3 on 2021-05-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0015_addblog_p_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('p_url', models.CharField(max_length=255)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]