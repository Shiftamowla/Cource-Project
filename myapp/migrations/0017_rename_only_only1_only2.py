# Generated by Django 5.1 on 2024-11-19 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_only_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='only',
            new_name='only1',
        ),
        migrations.CreateModel(
            name='only2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.author')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.coursemodel')),
                ('only1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.only1')),
            ],
        ),
    ]
