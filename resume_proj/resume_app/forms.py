from django import forms 
from .models import persnol_details , other_details


CHOICES = [
        ('1', 'Male'),
        ('2', 'Female'),
    ]
class persnol_details_form(forms.ModelForm):


    class Meta:

        model = persnol_details
        fields = ['name','dob','pin_code','state',
        'city','mobile','email','gender','address']


        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs ={'type':'date','class': 'form-control','placeholder': 'yyyy-mm-dd (DOB)'}),
            'gender':forms.RadioSelect(choices=CHOICES),
            'address':forms.Textarea(attrs={'name':'body','rows':5,'cols':35,'class':'form-control'}),
            'pin_code':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs ={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'})
        }


class other_details_form(forms.ModelForm):

    class Meta:

        model = other_details
        fields = ['objectives','skills','educations','certificates','hobies']
        widgets = {

            'objectives':forms.TextInput(attrs={'class':'form-control'}),
            'skills':forms.TextInput(attrs={'class':'form-control'}),
            'educations':forms.TextInput(attrs={'class':'form-control'}),
            'certificates':forms.TextInput(attrs={'class':'form-control'}),
            'hobies':forms.TextInput(attrs={'class':'form-control'})

        }
