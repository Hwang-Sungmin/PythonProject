from django.shortcuts import render
from django.http import HttpResponse
from itess.models import Topic, Information
from django.contrib.auth.models import User
import requests , re
# Create your views here.

java = Topic.objects.filter(name = '자바')
cloud = Topic.objects.filter(name = '클라우드')
Big_Data = Topic.objects.filter(name = '빅데이터')
IOT = Topic.objects.filter(name = 'IOT')
AI = Topic.objects.filter(name = 'AI')
python = Topic.objects.filter(name = '파이썬')
VR = Topic.objects.filter(name = 'VR')
C = Topic.objects.filter(name = 'C언어')

context = {
        'java' : java,
        'cloud' : cloud,
        'Big_Data' : Big_Data,
        'IOT' : IOT,
        'AI' : AI,
        'python' : python,
        'VR' : VR,
        'C' : C,
        'title' : {
            '자바': '',
            '클라우드': '',
            '빅데이터':'',
            'IOT':'',
            'AI':'',
            '파이썬':'',
            'VR':'', 
            'C언어':'',
        }
    }
def menu(request):
    return render(request, 'window/index.html', context)

def about(request):
    return render(request, 'window/about.html', context)    

def show(request, topic_title):        
    if( topic_title == "자바" ):
        return render(request, 'window/java.html', context)

#def link(request):
#    if request.method == "POST":
#        data = request.POST["link_address"]
#        print(data)
#        return HttpResponse(data)
          
    #print(request)
    #if request.method == "POST":
    #    data = request.POST["link_address"]
        # print(data.split('?'))
        # return HttpResponse(data.split('?')[1])
     