from django.contrib import admin

from scraper.models import Bookie, Sport, League, Adversary, Match

admin.site.register(Bookie)
admin.site.register(Sport)
admin.site.register(League)
admin.site.register(Adversary)
admin.site.register(Match)
