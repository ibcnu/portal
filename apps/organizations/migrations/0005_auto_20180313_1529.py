# Generated by Django 2.0.2 on 2018-03-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20180306_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='organizations.Address'),
        ),
    ]
