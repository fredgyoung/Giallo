from django.contrib import admin

from .models import Director, Actor, Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "country", "year")

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

