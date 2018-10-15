from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    logo = models.ImageField(null=True, blank=True, upload_to=settings.UPLOAD_DIR)
    members = models.CharField(max_length=512)
    photo = models.ImageField(null=True, blank=True, upload_to=settings.UPLOAD_DIR)

    def __unicode__(self):
        return self.name

class Rater(models.Model):
    user = models.OneToOneField(User)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username


YEAR_CHOICES = ( (2013,'2013'),(2014,'2014'),
    (2015,'2015'),('2016','2016')
)

RATING_CHOICES = ( (1,'1'),(2,'2'),
    (3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),
    (8,'8'),(9,'9'),(10,'10')
)


class Demo(models.Model):
    name = models.CharField(max_length=64)
    tagline = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    year = models.IntegerField(default=2014, choices=YEAR_CHOICES)
    url = models.URLField()
    live = models.BooleanField(default=True)
    github_url = models.URLField(null=True, blank=True)
    screenshot = models.ImageField(null=True, blank=True, upload_to=settings.UPLOAD_DIR)
    category = models.ForeignKey(Category)
    team = models.ForeignKey(Team)
    rating_count = models.IntegerField(default=0, blank=True)
    rating_sum = models.IntegerField(default=0, blank=True)

    def _get_average_rating(self):
        if self.rating_count == 0:
            return 0.0
        else:
            return round(float(self.rating_sum)/float(self.rating_count),1)

    rating_average = property(_get_average_rating)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    demo = models.ForeignKey(Demo)
    comment = models.CharField(max_length=512)
    score = models.IntegerField(default=1, choices=RATING_CHOICES)

    def __unicode__(self):
        return str(self.score) + ' ' + self.comment