from django.shortcuts import render
from django.http import HttpResponseRedirect
from app1.forms import StdForm
# Create your views here.
def AddNew(request):
    form=StdForm(request.POST,request.FILES)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect('/')
    context={'form':form}
    return render(request,'app1/upload.html',context)
def HomePage(request):
    return render(request,'app1/home.html')
