from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
def help(request):
    helpdict = {'help_insert':'Help page'}
    return render(request,'App_Two/help.html',context=helpdict)
