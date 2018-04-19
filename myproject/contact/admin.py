from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_adress', 'subject', 'message')

admin.site.register(Contact, ContactAdmin)

