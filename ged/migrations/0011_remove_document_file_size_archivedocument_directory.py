# Generated by Django 5.0.6 on 2024-06-05 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ged', '0010_remove_archivedocument_uploaded_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file_size',
        ),
        migrations.AddField(
            model_name='archivedocument',
            name='directory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ged.directory'),
            preserve_default=False,
        ),
    ]
