# Generated by Django 5.1 on 2024-08-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_alter_batch_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='students',
            field=models.ManyToManyField(related_name='students', to='myapp.student'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='myapp.teacher'),
        ),
    ]
