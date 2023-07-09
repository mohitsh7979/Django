from import_export import resources 
from .models import referral

class ReportResource(resources.ModelResource):
     class Meta:
         model = referral