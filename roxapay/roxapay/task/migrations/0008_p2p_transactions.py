# Generated by Django 4.2.8 on 2024-03-04 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0007_task_partakers'),
    ]

    operations = [
        migrations.CreateModel(
            name='P2P_transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_handler', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pay', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now=True)),
                ('owner_accept', models.BooleanField(default=False)),
                ('owner_cancel', models.BooleanField(default=False)),
                ('handler_complete', models.BooleanField(default=False)),
                ('handler_cancel', models.BooleanField(default=False)),
                ('period', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
                ('Task_owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]