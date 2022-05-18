from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):

    COUNTRY_CHOICES = [
        ('GE', 'Germany'),
        ('IT', 'Italy'),
        ('SP', 'Spain'),
        ('US', 'United States'),
    ]

    title = models.CharField(max_length=255)
    alternate_titles = models.CharField(max_length=255, null=True, blank=True)
    director = models.ForeignKey('Director', null=True, blank=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', null=True, blank=True, )
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    year = models.SmallIntegerField()

    # Information Links
    wikipedia_link = models.URLField(null=True, blank=True)
    imdb_link = models.URLField(null=True, blank=True)
    rotten_tomatoes_link = models.URLField(null=True, blank=True)

    # Streaming Links
    amazon_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    tubi_link = models.URLField(null=True, blank=True)
    # netflix =

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
