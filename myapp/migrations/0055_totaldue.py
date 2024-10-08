# Generated by Django 5.1 on 2024-08-31 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0054_delete_totaldue'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalDue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='total_due', to='myapp.student')),
            ],
        ),
    ]
