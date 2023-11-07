# Generated by Django 4.2.6 on 2023-10-25 00:50

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('title', models.CharField(max_length=300)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', primary_key=True, serialize=False)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='about',
            field=models.TextField(null=True),
        ),
    ]