# Generated by Django 3.1.3 on 2020-12-08 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_subscrition'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscrition',
            new_name='Subscription',
        ),
    ]