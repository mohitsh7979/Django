from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import ReportResource 
from .models import *

# Register your models here.

# admin.site.register(User)

class ReportAdmin(ImportExportModelAdmin):
     resource_class = ReportResource      
     
# admin.site.register(referral, ReportAdmin)

@admin.register(referral)

class referral(admin.ModelAdmin):
    list_display = ["id" , "name" ,"email" ,"course" ,"fees","own_referal","referal_code","date"]




@admin.register(referral_table)

class referral_admin(admin.ModelAdmin):
    list_display = ["id" , "referrer_id" , "referred_id" , "referral_code"]



@admin.register(commission)

class commission_admin(admin.ModelAdmin):
    list_display = ["id" , "user_id" , "name" , "email" ,"commission_amount" , "referral_table_id" , "commission_date" ]



