from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Tourning)
admin.site.register(models.StarsReview)
admin.site.register(models.Category)

# Register your models here.
