from django.shortcuts import render, HttpResponse, redirect
from .models import Farmer
from .forms import EmployeeForm

# Create your views here.


def farmer(request):
<<<<<<< HEAD

      if request.method=="POST":
=======
    if request.method=="POST":
>>>>>>> 780c507 (this is new commit)
        a=request.POST['search']
        all=Farmer.objects.filter(Name=a)
        return render(request,'index.html',{'all':all})
    
<<<<<<< HEAD
      all = Farmer.objects.all()


      return render(request, 'Admin/Farmer/Add', {'all': all})
    

    


def update(request, id):
    
      
      if request.method == "POST":
=======
    all = Farmer.objects.all()


    return render(request, 'Admin/Farmer/Add', {'all': all})


def update(request, id):
    if request.method == "POST":
>>>>>>> 780c507 (this is new commit)
        data = EmployeeForm(data=request.POST)
        updatedata = Farmer.objects.filter(id=id)
        print(updatedata)
        if data.is_valid():
            for i in updatedata:
                i.Name = data.cleaned_data['Name']
                i.Mobile_No = data.cleaned_data['Mobile_NO']
                i.Whatsapp_No = data.cleaned_data['Whatsapp_No']
                i.Village = data.cleaned_data['Village']
                i.District = data.cleaned_data['District']
                i.Pin_code = data.cleaned_data['Pin_code']
                i.save()

            return redirect("/Admin/Farmer/View")
<<<<<<< HEAD
      else:
=======
    else:
>>>>>>> 780c507 (this is new commit)

        a = Farmer.objects.filter(id=id)


<<<<<<< HEAD
      return render(request,'admin/update_farmer.html',{'a':a})
    



def delete(request,id):

  
      delete_data=Farmer.objects.filter(id=id)
      delete_data.delete()
      return redirect("/Admin/Farmer/View")
    


def farmer_detail(request):

 

     if request.method == "POST":
=======
    return render(request,'admin/update_farmer.html',{'a':a})


def delete(request,id):
    delete_data=Farmer.objects.filter(id=id)
    delete_data.delete()
    return redirect("/Admin/Farmer/View")

def farmer_detail(request):

    if request.method == "POST":
>>>>>>> 780c507 (this is new commit)
        a = EmployeeForm(data=request.POST)

        if a.is_valid():
            Name = a.cleaned_data['Name']
            Mobile_No = a.cleaned_data['Mobile_NO']
            Whatsapp_No = a.cleaned_data['Whatsapp_No']
            Village = a.cleaned_data['Village']
            District = a.cleaned_data['District']
            Pin_code = a.cleaned_data['Pin_code']

            Farmer(Name=Name, Mobile_No=Mobile_No, Whatsapp_No=Whatsapp_No,
                   Village=Village, District=District, Pin_code=Pin_code).save()

            return redirect("/Admin/Farmer/View")

<<<<<<< HEAD
     farmer = EmployeeForm()
     return render(request,'admin/add_farmer.html',{'farmer':farmer})
    
  




=======
    a = EmployeeForm()

    return render(request, 'farmer/former_detail.html', { 'a': a})


def search(request):
    if request.method=="POST":
        a=request.POST['search']
        print(a)
        b=Farmer.objects.filter(Name=a)
        print(b)
>>>>>>> 780c507 (this is new commit)





