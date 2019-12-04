from django.db import models
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail
import re
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    
class Information(models.Model):
    title = models.CharField(max_length=300)
    academy = models.CharField(max_length=300)
    info = models.CharField(max_length=300)

    training_date = models.CharField(max_length= 300)
    pay = models.CharField(max_length= 300)
    wage = models.CharField(max_length= 300)
    people = models.CharField(max_length= 300)
    training_time = models.CharField(max_length= 300)
    
    code = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='courses')

def get_data(*keywords):
    import requests
    from bs4 import BeautifulSoup
    
    for keyword in keywords:
        if not Topic.objects.filter(name=keyword):#없으면
            Topic.objects.create(name=keyword)#없으면 생성
        topic = Topic.objects.get(name=keyword)
        for i in range(1, 100):
            res = requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do", params={
                'searchTotalKeyword': topic.name,
                'pageIndex': i, 
            })
            data = BeautifulSoup(res.text, 'html.parser')
            if data.select('p[class=name]'):# 값이 있으면 
                for title in data.select('p[class=name]'):
                    Information.objects.create(
                        title=title.text.strip(),
                        topic = topic
                    )  
                for academy in data.select('dl[class=academy]'):
                    Information.objects.create(
                        academy=academy.text.strip(),
                        topic = topic
                    )  
                for info in data.select('ul[class=info]'):
                    Information.objects.create(
                        info=info.text.strip(),
                        topic = topic
                    )  #searchForm1 > div > div > ul > li:nth-child(2) > div.cont > ul:nth-child(3) > li:nth-child(1)
                for training_date in data.select("#searchForm1 > div > div > ul > li:nth-child(2) > div.cont > ul:nth-child(3) > li:nth-child(1)") :
                    Information.objects.create(          
                        training_date=training_date.text.strip(),             
                        topic = topic
                    )  

                
            else:
                break
