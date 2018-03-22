# Generated by Django 2.0.2 on 2018-03-21 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='short_text',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
