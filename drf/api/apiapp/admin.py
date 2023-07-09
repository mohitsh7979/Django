from django.contrib import admin
from .models import apimodel

# Register your models here.


@admin.register(apimodel)

class apiadmin(admin.ModelAdmin):

    list_display = ['id','name','f_name','mobile_no','address']
