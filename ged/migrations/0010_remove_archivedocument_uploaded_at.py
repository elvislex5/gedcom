# Generated by Django 5.0.6 on 2024-06-04 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ged', '0009_archivedocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivedocument',
            name='uploaded_at',
        ),
    ]