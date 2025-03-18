# Generated by Django 5.1.7 on 2025-03-16 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0010_alter_advertisment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 16, 9, 41, 54, 480247)),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('tech', 'Техника'), ('wear', 'Одежда'), ('food', 'Еда'), ('other', 'Разное')], max_length=10),
        ),
    ]
