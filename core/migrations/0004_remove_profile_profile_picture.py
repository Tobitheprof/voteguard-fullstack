# Generated by Django 4.2.6 on 2023-11-07 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_blogpost_author_alter_blogpost_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
