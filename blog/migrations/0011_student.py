# Generated by Django 3.1.3 on 2021-01-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201208_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
            ],
        ),
    ]
