# Generated by Django 3.2.3 on 2021-05-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_auto_20210527_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='addblog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Decri', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]