from django import forms

class EmployeeForm(forms.Form):
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Mobile_NO=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Whatsapp_No=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Village=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    District=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Pin_code=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    

