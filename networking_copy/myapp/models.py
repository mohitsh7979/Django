from django.db import models


class referral(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50)
    fees = models.IntegerField()
    own_referal = models.CharField(max_length=100 , unique=True , null=True , blank=True)
    referal_code = models.CharField(max_length=100 , null=True , blank=True)
    date = models.DateField(null=True)


    def __str__(self):
        return self.name
    

        


class referral_table(models.Model):
    referrer_id = models.ForeignKey(referral , related_name='referrer_referral_set' ,on_delete=models.CASCADE)
    referred_id = models.ForeignKey(referral , related_name='referred_referral_set' , on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=50)

  


class commission(models.Model):
    user_id = models.ForeignKey(referral , related_name='referrer_commission_set' ,on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    commission_amount = models.IntegerField()
    referral_table_id = models.ForeignKey(referral_table , related_name='referral_commission_set' , on_delete=models.CASCADE) 
    commission_date = models.DateField(null=True)


    def __str__(self):
        return self.user_id.name




    






