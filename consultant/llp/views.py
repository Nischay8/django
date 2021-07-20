
from .forms import login_regis,signup_form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import login, signup

# Create your views here.
def homepage(request):
    if request.method=='POST':
        fm=login_regis(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=login_regis()
    stud=login.objects.all()
    return render(request,'home.html',{'form':fm,'stu':stud})


def signup_page(request):
    if request.method=='POST':
        sp=signup_form(request.POST)
        if sp.is_valid():
            sp.save()
    else:
        sp=signup_form()
    spd=signup.objects.all()
    return render(request,'signup.html',{'sign':sp,'signupd':spd})

def table_data(request):
    userd=signup.objects.all()
    return render(request,'userdetail.html',{'tyu':userd})
    
def delete_data(request,id):
    if request.method=='POST':
        pi=signup.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#this function will update
def update_data(request,id):
    if request.method=='POST':
        pi=signup.objects.get(pk=id)
        fm=signup_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save() 
    else:
        pi=signup.objects.get(pk=id)
        fm=signup_form(instance=pi)
    return render(request,'updatestudent.html',{'id':id,'form':fm})