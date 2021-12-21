# Generated by Django 3.1.3 on 2020-12-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_customerreportrecord_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerreportrecord',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerreportrecord',
            name='published',
            field=models.DateTimeField(),
        ),
    ]