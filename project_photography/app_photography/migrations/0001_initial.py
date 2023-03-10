# Generated by Django 4.1.5 on 2023-01-12 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_desc', models.TextField(max_length=200)),
                ('task_category', models.CharField(max_length=100)),
                ('task_assign_date', models.DateField(default=datetime.datetime.now)),
                ('task_end_date', models.DateField(blank=True, default=0, null=True)),
                ('task_assign_to', models.CharField(max_length=200)),
                ('task_assigned_by', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 1, 12, 16, 24, 39, 21134))),
                ('updated_at', models.DateTimeField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'tbl_task',
            },
        ),
    ]
