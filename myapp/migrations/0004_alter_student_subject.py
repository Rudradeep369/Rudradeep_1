# Generated by Django 5.1 on 2024-08-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_student_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.CharField(default='All', max_length=100),
        ),
    ]
