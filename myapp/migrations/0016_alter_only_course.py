# Generated by Django 5.1 on 2024-11-19 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_only'),
    ]

    operations = [
        migrations.AlterField(
            model_name='only',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.coursemodel'),
        ),
    ]
