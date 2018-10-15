from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    def save(self, *args, **kwargs):  # this is to override the parent class's save function
        #uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
            #self.slug=slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    #@property
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
