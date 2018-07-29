# Generated by Django 2.0.4 on 2018-05-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
