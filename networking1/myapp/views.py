from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
import uuid
from django.db.models import Q
from .models import *
from django.db.models import Sum


# Create your views here.

def generate_referral_code(request):
    return HttpResponse(str(uuid.uuid4().hex)[:10])


def loginhandle(request):

    if request.method == "POST":

        a = AuthenticationForm(data=request.POST)

        if a.is_valid():

            uname = a.cleaned_data['username']
            passw = a.cleaned_data['password']

            user = authenticate(username=uname, password=passw)

            if user is not None:

                login(request, user)

                a = request.user

                return redirect("/show/")

    else:

        a = AuthenticationForm()

        return render(request, 'login.html', {'a': a})


def showdata(request):

    a1_code = referral.objects.all()   # we collect all data in referral tabel

    for i in a1_code:                  #

        for j in a1_code:

            # we check that own referal code is equal referal code if it is equal at the we save our data into a referal table
            if (i.own_referal == j.referal_code):

                # we collect all data in referal table because we want that is data is already save in referal table that time we have to need again save data into a referal table
                a2_code = referral_table.objects.all()

                flag = 0

                for k in a2_code:

                    # we check if data is equal our referal table data at the time we does not store data into a table
                    if (k.referrer_id == i and k.referred_id == j):

                        print(k.referrer_id, k.referred_id, "=", i, j)

                        flag = 1
                        break

                if (flag != 1):        # if flag is not equal not one at time we have to need storing a data into a referal table

                    referral_table(referrer_id=i,  referred_id=j,
                                   referral_code=j.referal_code).save()

                else:

                    print("Already saved !!!")

    # commission calculation

    data = referral_table.objects.all()

    for i in data:

        new_flag = 0

        p = commission.objects.all()

        for j in p:

            if (j.user_id == i.referrer_id and j.referral_table_id == i):

                new_flag = 1

        if (new_flag != 1):

            print("This is my ", i.referred_id.date)

            commission(user_id=i.referrer_id, name = i.referrer_id.name, email = i.referrer_id.email, commission_amount=(
                (i.referred_id.fees)*5)/100,  referral_table_id=i, commission_date=i.referred_id.date).save()
            commission(user_id=i.referred_id, name = i.referred_id.name , email = i.referred_id.email ,commission_amount=(
                (i.referred_id.fees)*10)/100,  referral_table_id=i, commission_date=i.referred_id.date).save()

        else:

            print("commision data already saved !!!")

    commission_data = commission.objects.all()

    # third chain

    q = referral.objects.all()

    w = referral_table.objects.all()

    for i in q:

        for j in w:

            if (i == j.referrer_id):

                e = j.referred_id

                for k in w:
                    if (e == k.referrer_id):

                        p = commission.objects.all()

                        new_f = 0

                        for m in p:

                            if (m.user_id == i and m.name == i.name and m.email == i.email and m.commission_amount == ((k.referred_id.fees)*2.5)/100 and m.referral_table_id == k):

                                new_f = 1

                        if (new_f != 1):

                            commission(user_id=i, name= i.name , email = i.email , commission_amount=(
                                (k.referred_id.fees)*2.5)/100, referral_table_id=k).save()

                        else:

                            print("Already saved !!!!")

                        return redirect("/commision_count/")

    # return render(request, 'table.html', {'data': commission_data})


def desc(request, id):

    c = commission.objects.filter(id=id)

    return render(request, 'desc.html', {'c': c})




def search(request):


        if 'q' in request.GET:
            q = request.GET['q']
            print("this is q>>>",q)
            date_q = Q(Q(commission_date__icontains=q))
            print("this is date q___>>>>>",date_q)

            all = commission.objects.filter(date_q)
            print("all", len(all))

            if (len(all) != 0):
                return render(request, 'table.html', {'data': all})



def commission_count(request):
    p = commission.objects.values('email','name','user_id').annotate(total_amount=Sum('commission_amount'))

    print(p)
    
    return render(request,'table.html',{'p':p})



   