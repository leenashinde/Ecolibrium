# Generated by Django 3.1.1 on 2020-09-09 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'director',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('popularity', models.FloatField()),
                ('imdb_score', models.FloatField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.director')),
                ('genre', models.ManyToManyField(related_name='movie_category', to='movie.Category')),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
    ]
