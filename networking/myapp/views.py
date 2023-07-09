from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import User, Referral, Commission
from .forms import ReferralSignUpForm, ReferralForm


def signup(request):
    if request.method == 'POST':
        form = ReferralSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            referral_code = form.cleaned_data.get('referral_code')
            referral = Referral.objects.create(referrer=user, referred_email=user.email, referred_name=user.username, referral_code=referral_code)
            referral.save()
            commission = Commission.objects.create(user=user, commission_amount=10)
            commission.save()
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('dashboard')
    else:
        form = ReferralSignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    commissions = user.commissions_earned.all()
    return render(request, 'dashboard.html', {'commissions': commissions})


@login_required
def invite(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referred_email = form.cleaned_data['referred_email']
            referred_name = form.cleaned_data['referred_name']
            referral_code = request.user.referral_code
            referral = Referral.objects.create(referrer=request.user, referred_email=referred_email, referred_name=referred_name, referral_code=referral_code)
            referral.save()
            messages.success(request, 'Invitation sent successfully')
            return redirect('dashboard')
    else:
        form = ReferralForm()
    return render(request, 'invite.html', {'form': form})