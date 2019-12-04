from django.shortcuts import render
from itess.models import Topic, Information
import requests , re
# Create your views here.

def show(request):
    java = Topic.objects.filter(name = '자바')
    cloud = Topic.objects.filter(name = '자바')
    Big_Data = Topic.objects.filter(name = '자바')
    IOT = Topic.objects.filter(name = '자바')
    AI = Topic.objects.filter(name = '자바')
    python = Topic.objects.filter(name = '자바')
    VR = Topic.objects.filter(name = '자바')
    C = Topic.objects.filter(name = '자바')


    context = {
        'java' : java,
        'cloud' : cloud,
        'Big_Data' : Big_Data,
        'IOT' : IOT,
        'AI' : AI,
        'python' : python,
        'VR' : VR,
        'C' : C,

    }
    return render(request, 'window/index.html', context)
    #return render(request, 'window/index.html', context)

def test(request):
    return render(request, 'test.html')