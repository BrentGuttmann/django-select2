from django.contrib import admin
from .models import Genre
from .models import Artist
from .models import Album
from .models import Country
from .models import City
from .models import Groupie

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Groupie)
class GroupieAdmin(admin.ModelAdmin):
    pass
