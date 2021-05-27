# Generated by Django 3.2.3 on 2021-05-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=255)),
                ('L_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
