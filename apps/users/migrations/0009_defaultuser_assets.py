# Generated by Django 2.0.2 on 2018-03-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180307_1827'),
        ('users', '0008_auto_20180312_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultuser',
            name='assets',
            field=models.ManyToManyField(to='assets.Asset'),
        ),
    ]
