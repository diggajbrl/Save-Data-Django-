from django.contrib import admin

# Register your models here.

from app.models import Myform

class formAdmin (admin.ModelAdmin) :
    list_display = ('first_name', 'last_name', 'my_email')

admin.site.register(Myform, formAdmin)