from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Referral


class ReferralSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    referral_code = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'referral_code')

    def clean_referral_code(self):
        referral_code = self.cleaned_data.get('referral_code')
        try:
            Referral.objects.get(referral_code=referral_code)
        except Referral.DoesNotExist:
            raise forms.ValidationError('Invalid referral code')
        return referral_code


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ('referred_email', 'referred_name')