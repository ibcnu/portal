# Generated by Django 2.0.2 on 2018-03-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_remove_comment_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='short_text',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
