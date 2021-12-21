# Generated by Django 3.1.3 on 2020-12-01 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('world', 'WORLD'), ('environment', 'ENVIRONMENT'), ('technology', 'TECHNOLOGY'), ('design', 'DESIGN'), ('culture', 'CULTURE'), ('business', 'BUSINESS'), ('politics', 'POLITICS'), ('opinion', 'OPINION'), ('science', 'SCIENCE'), ('health', 'HEALTH'), ('style', 'STYLE'), ('travel', 'TRAVEL')], default='WORLD', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('heading', models.CharField(max_length=200)),
                ('comment_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]