# Generated by Django 5.1 on 2024-08-30 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0053_rename_std_total_due_totaldue'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TotalDue',
        ),
    ]
