# Generated by Django 2.0.2 on 2018-03-27 21:24

import apps.files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20180327_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=apps.files.models.upload_to),
        ),
    ]
