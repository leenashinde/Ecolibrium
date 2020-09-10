# Generated by Django 3.1.1 on 2020-09-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='name',
        ),
        migrations.AddField(
            model_name='director',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
