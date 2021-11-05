from django.contrib import admin

from .models import Person
from .models import Equipment

admin.site.register(Person)
admin.site.register(Equipment)