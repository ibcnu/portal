# Generated by Django 2.0.2 on 2018-03-13 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180307_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='organizations.Company'),
        ),
    ]