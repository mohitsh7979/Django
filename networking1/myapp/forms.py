from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

import uuid


class addstudentdetails_form(forms.ModelForm):

    
    class Meta:

        model = referral
        fields = ["name", "email", "course",
                  "fees", "own_referal", "referal_code"]
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

            'course': forms.TextInput(attrs={'class': 'form-control'}),

            'fees': forms.TextInput(attrs={'class': 'form-control'}),

            'referal_code': forms.TextInput(attrs={'class': 'form-control'}),


            'own_referal': forms.TextInput(attrs={'value': str(uuid.uuid4().hex)[:10] , 'class' :'form-control'})
        }


class referral_form(forms.Form):

    referral_code = forms.CharField()
