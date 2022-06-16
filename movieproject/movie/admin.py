from django.contrib import admin
from movie.models import Moviemodel
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['Releasedate', 'Name','Actor','Actress','Ratings']

admin.site.register(Moviemodel,MovieAdmin)