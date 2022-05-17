from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    text={'name':'shahinur','course':'project'}
    return render(request,'index.html',text)

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    values=val1+val2
    return render(request,'result.html',{'result':values})

def shop(request):
    return HttpResponse('welcome bangladesh')