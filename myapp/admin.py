from django.contrib import admin
from .models import contact
# Register your models here.

class adminmodel(admin.ModelAdmin):
    list_display=['name','email','message']


admin.site.register(contact,adminmodel)