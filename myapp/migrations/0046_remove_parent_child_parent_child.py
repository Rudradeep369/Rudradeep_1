# Generated by Django 5.1 on 2024-08-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_payment_due_amount_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='child',
        ),
        migrations.AddField(
            model_name='parent',
            name='child',
            field=models.ManyToManyField(related_name='parent', to='myapp.student'),
        ),
    ]
