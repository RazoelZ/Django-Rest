from django.contrib import admin
from belajarcurd.models import Hero


class HeroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hero, HeroAdmin)
