from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
# Convert to ASCII. Convert spaces to hyphens. Remove characters that aren't
# alphanumerics, underscores, or hyphens. Convert to lowercase. Also strip
# leading and trailing whitespace
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers


User = get_user_model()

category_choices = (

  ('world','WORLD'),
  ('environment','ENVIRONMENT'),
  ('technology','TECHNOLOGY'),
  ('design','DESIGN'),
  ('culture','CULTURE'),
  ('business','BUSINESS'),
  ('politics','POLITICS'),
  ('opinion','OPINION'),
  ('science','SCIENCE'),
  ('health','HEALTH'),
  ('style','STYLE'),
  ('travel','TRAVEL')

)


# class Category(models.Model):
  # title = models.CharField(max_length=150, choices=category_choices  , default="WORLD" )

  # class Meta:
  #     verbose_name_plural = "Categories"
  #     ordering=["title"]

  # def __str__(self):
  #   return self.title



# Create your models here.
class Post(models.Model):
  title  = models.CharField(max_length=250)
  category = models.CharField(max_length=100 , choices=category_choices , default = "World")
  image = models.FileField(upload_to="photos/%Y/%m/%d/")
  excerpt =  models.TextField(null=True)
  content =  models.TextField(null=True)
  slug = models.SlugField(max_length=200 , unique_for_date = 'published')
  published = models.DateTimeField(default=timezone.now) 
  date_created = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User , on_delete=models.CASCADE , related_name = "blog_post" )
  comment_count = models.IntegerField(default=0)
  like_count = models.IntegerField(default=0)
  featured = models.BooleanField(default=False)

  class Meta : 
    ordering = ['-published']
    # unique_together = ['album', 'order']

  def __str__(self):
    return self.title



class Subscription(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length = 100)

  def __str__(self):
    return self.email


class CustomerReportRecord(models.Model):
        age = models.IntegerField()
        published = models.DateTimeField()
        reference = models.CharField(unique=True, max_length=20)
        description = models.TextField()

        def __str__(self):
          return self.reference




def check_city(city):
  if city != "lekki":
    raise serializers.ValidationError('City must be lekki')
  else:
    return  city
class Student(models.Model):
      name = models.CharField(max_length=40)
      roll = models.IntegerField()
      city = models.CharField(max_length = 40 , validators = [check_city])
      
      
      def __str__(self):
          return self.name