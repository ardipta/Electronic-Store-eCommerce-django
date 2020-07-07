from django.contrib import admin

from computers.models import Desktop, Laptop

admin.site.register(Laptop)
admin.site.register(Desktop)
