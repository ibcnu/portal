# Generated by Django 2.0.2 on 2018-03-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_auto_20180307_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
