# Generated by Django 4.0.3 on 2022-05-08 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0002_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='image',
            new_name='imagen',
        ),
    ]
