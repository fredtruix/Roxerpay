# Generated by Django 4.2.8 on 2024-03-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_rename_task_owner_p2p_transactions_task_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='p2p_transactions',
            name='task_owner_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
