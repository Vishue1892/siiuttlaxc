# Generated by Django 5.0.6 on 2024-07-04 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
