from django.contrib import admin
from .models import Directors, Actors, Movies

admin.site.register(Movies)
admin.site.register(Directors)
admin.site.register(Actors)
