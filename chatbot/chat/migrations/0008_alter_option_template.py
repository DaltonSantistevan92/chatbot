# Generated by Django 4.1.7 on 2023-03-24 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_option_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='template',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.decisiontemplate'),
        ),
    ]
