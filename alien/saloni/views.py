from django.shortcuts import render,HttpResponse

# Create your views here.


def a(request):
    return render(request,'saloni.html')



def b(request):
    # a=10
    # b=20
    # c=a+b
    # return HttpResponse(c)
    return render(request,'mohit.html')