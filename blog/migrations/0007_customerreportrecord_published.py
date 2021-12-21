# Generated by Django 3.1.3 on 2020-12-04 01:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_customerreportrecord_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerreportrecord',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
