# Generated by Django 4.1.5 on 2023-01-14 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='years_averagesalary',
            old_name='year',
            new_name='years',
        ),
    ]