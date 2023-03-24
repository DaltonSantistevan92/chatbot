# Generated by Django 4.1.7 on 2023-03-24 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_option_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ERROR', 'Error'), ('SUCCESS', 'Success')], default='PENDING', max_length=9)),
                ('user_input', models.CharField(max_length=100)),
                ('prompt', models.TextField(blank=True, default=None, null=True)),
                ('answer', models.TextField(blank=True, default=None, null=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.decisiontemplate')),
            ],
        ),
    ]
