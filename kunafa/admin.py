from django.contrib import admin
from .models import Kunafa, Crunchy_kunafa, Baklawa, Topping

# Register your models here.

admin.site.register(Kunafa)
admin.site.register(Baklawa)
admin.site.register(Crunchy_kunafa)
admin.site.register(Topping)