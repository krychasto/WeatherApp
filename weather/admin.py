from django.contrib import admin
from .models import Temperature, Favorite

# Register your models here.

admin.site.register(Temperature)
admin.site.register(Favorite)