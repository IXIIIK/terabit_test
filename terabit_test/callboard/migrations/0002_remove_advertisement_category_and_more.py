# Generated by Django 5.1.7 on 2025-03-15 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='category',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='application',
            name='advertisement',
        ),
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Advertisement',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
