# Generated by Django 4.0.4 on 2022-05-18 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giallo', '0004_alter_movie_actors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title']},
        ),
    ]
