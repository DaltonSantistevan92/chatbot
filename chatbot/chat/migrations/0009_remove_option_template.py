# Generated by Django 4.1.7 on 2023-03-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_option_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='template',
        ),
    ]