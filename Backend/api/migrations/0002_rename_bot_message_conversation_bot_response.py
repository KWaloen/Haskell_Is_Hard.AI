# Generated by Django 5.1.1 on 2024-10-23 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='bot_message',
            new_name='bot_response',
        ),
    ]
