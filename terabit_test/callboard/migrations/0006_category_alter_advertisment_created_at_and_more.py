# Generated by Django 5.1.7 on 2025-03-16 09:21

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0005_alter_advertisment_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tech', 'Техника'), ('wear', 'Одежда'), ('food', 'Еда'), ('other', 'Разное')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 16, 9, 21, 35, 157554)),
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.category'),
        ),
    ]
