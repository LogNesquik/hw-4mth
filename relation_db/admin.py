from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Touring)
admin.site.register(models.Review)
admin.site.register(models.Tag)

# Register your models here.
