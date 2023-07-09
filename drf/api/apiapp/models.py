from django.db import models



class apimodel(models.Model):

    name = models.CharField(max_length=30)
    f_name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
