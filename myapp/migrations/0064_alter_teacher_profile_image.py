# Generated by Django 5.1 on 2024-09-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0063_alter_teacher_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/teacher-img/'),
        ),
    ]
