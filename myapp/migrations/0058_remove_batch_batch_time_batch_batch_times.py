# Generated by Django 5.1 on 2024-09-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0057_payment_modification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='batch_time',
        ),
        migrations.AddField(
            model_name='batch',
            name='batch_times',
            field=models.JSONField(default=dict),
        ),
    ]
