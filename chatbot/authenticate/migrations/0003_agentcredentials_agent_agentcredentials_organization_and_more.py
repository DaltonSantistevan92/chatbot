# Generated by Django 4.1.7 on 2023-03-24 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_agent_agentengine_agentcredentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentcredentials',
            name='agent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authenticate.agent'),
        ),
        migrations.AddField(
            model_name='agentcredentials',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authenticate.organization'),
        ),
        migrations.AddField(
            model_name='agentengine',
            name='agent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authenticate.agent'),
        ),
    ]