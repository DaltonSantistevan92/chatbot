# Generated by Django 4.1.7 on 2023-03-24 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='function',
            old_name='owner',
            new_name='organization',
        ),
    ]
