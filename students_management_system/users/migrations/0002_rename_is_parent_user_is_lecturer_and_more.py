# Generated by Django 5.0.6 on 2024-07-08 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_parent',
            new_name='is_lecturer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]
