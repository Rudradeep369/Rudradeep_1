# Generated by Django 5.1 on 2024-08-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_batch_batch_duration_alter_batch_class_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_duration',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='batch',
            name='class_level',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='batch',
            name='class_mode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='batch',
            name='teacher_name',
            field=models.CharField(max_length=100),
        ),
    ]
