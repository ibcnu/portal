# Generated by Django 2.0.2 on 2018-03-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='slug',
            field=models.SlugField(default='123_main'),
            preserve_default=False,
        ),
    ]
