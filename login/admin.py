from django.contrib import admin
from . import models

class userlogin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]
admin.site.register(models.login, userlogin)