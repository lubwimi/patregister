from django.contrib import admin
from .models import Patmos

class PatmosAdmin(admin.ModelAdmin):
    list_display = ['fornamn', 'efternamn', 'personnummer', 'adress', 'telefon', 'dopdatum', 'ankomstdatum', 'uttrade', 'gift_med', 'ogift']

# Register your models here.

admin.site.register(Patmos, PatmosAdmin)

