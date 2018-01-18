# Generated by Django 2.0.1 on 2018-01-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Space_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.TextField(max_length=2000)),
                ('date', models.DateTimeField(auto_now=True)),
                ('explanation', models.TextField(max_length=2000)),
                ('hdurl', models.CharField(max_length=180)),
                ('media_type', models.TextField(max_length=50)),
                ('service_version', models.CharField(max_length=2)),
                ('title', models.TextField(max_length=50)),
                ('url', models.CharField(max_length=180)),
            ],
        ),
    ]
