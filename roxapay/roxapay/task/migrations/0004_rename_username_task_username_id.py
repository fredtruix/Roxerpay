# Generated by Django 4.2.8 on 2024-01-31 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_task_task_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='username',
            new_name='username_id',
        ),
    ]
