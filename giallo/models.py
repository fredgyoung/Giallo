from django.db import models

class Directors(models.Model):
    name = models.CharField(max_length=255)

class Actors(models.Model):
    name = models.CharField(max_length=255)

class Movies(models.Model):

    COUNTRY_CHOICES = [
        ('GE', 'Germany'),
        ('IT', 'Italy'),
        ('SP', 'Spain'),
        ('US', 'United States'),
    ]

    title = models.CharField(max_length=255)
    alternate_titles = models.CharField(max_length=255)
    director = models.ForeignKey('Directors', null=True, blank=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actors')
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    year = models.SmallIntegerField()
    youtube_link = models.URLField()
    '''
    netflix, tubi, 
    '''


