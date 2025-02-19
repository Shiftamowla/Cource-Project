# Generated by Django 5.1.3 on 2024-11-18 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_courseeemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeemodel',
            name='Course_title',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='featured_video',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='courseeemodel',
            name='status',
        ),
        migrations.AddField(
            model_name='courseeemodel',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.coursemodel'),
        ),
        migrations.AddField(
            model_name='courseeemodel',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.lesson'),
        ),
    ]
