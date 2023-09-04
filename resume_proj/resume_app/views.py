from django.shortcuts import render
from .forms import persnol_details_form,other_details_form

# Create your views here.


def persnol(request):
    p_form = persnol_details_form()
    o_form = other_details_form()
    return render(request,'index.html',{'p_form':p_form,'o_form':o_form})


