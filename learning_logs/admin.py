from django.contrib import admin

# Register the models here!

from .models import *

admin.site.register(Topic)
admin.site.register(Entry)