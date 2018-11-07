from django.contrib import admin
from .models import Machine,Operation,Component, Stats

admin.site.register(Machine)
admin.site.register(Operation)
admin.site.register(Component)
admin.site.register(Stats)