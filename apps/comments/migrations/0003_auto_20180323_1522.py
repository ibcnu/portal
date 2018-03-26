# Generated by Django 2.0.2 on 2018-03-23 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('comments', '0002_auto_20180321_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='allow_annon',
            new_name='allow_anonymous',
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
