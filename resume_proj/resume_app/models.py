from django.db import models

# Create your models here.


STATE_CHOICES = {

    ('Rajasthan','Rajasthan'),
    ('Punjab','Punjab'),
    ('Bihar','Bihar'),
    ('Haryana','Haryana')
}


class persnol_details(models.Model):

    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    pin_code = models.PositiveIntegerField()
    state = models.CharField(max_length=50,choices=STATE_CHOICES)
    city = models.CharField(max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    # profile_img = models.ImageField(upload_to='media')

class other_details(models.Model):
    
    objectives = models.CharField(max_length=300)
    skills = models.CharField(max_length=100)
    educations = models.CharField(max_length=100)
    certificates = models.CharField(max_length=100)
    hobies = models.CharField(max_length=100)



