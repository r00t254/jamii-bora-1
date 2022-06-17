from django.contrib import admin
from .models import Profile,Business,NeighbourHood

# Register your models here.

admin.site.register(NeighbourHood)
admin.site.register(Profile)
admin.site.register(Business)

