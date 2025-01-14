# Generated by Django 5.1.3 on 2024-11-17 04:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creatorprofilemodel',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='Display_name',
        ),
        migrations.RemoveField(
            model_name='viewerprofilemodel',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='viewerprofilemodel',
            name='Skills',
        ),
        migrations.AddField(
            model_name='custom_user',
            name='Image',
            field=models.ImageField(null=True, upload_to='Media/user_Pic'),
        ),
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_title', models.CharField(max_length=255, null=True)),
                ('Price', models.TextField(max_length=10, null=True)),
                ('Category', models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], max_length=255, null=True)),
                ('Course_Description', models.TextField(max_length=255, null=True)),
                ('Image', models.ImageField(null=True, upload_to='Media/Course_Pic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='JobModel',
        ),
    ]
