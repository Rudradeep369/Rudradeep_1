# Generated by Django 5.1 on 2024-08-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
