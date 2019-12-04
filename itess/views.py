from django.shortcuts import render
from bs4 import BeautifulSoup
import requests , re
from .models import Information, Topic
# Create your views here.

def get_infos(request):
    topics = Topic.objects.all()
    context = {
        'topics' : topics
    }
    return render(request,'itess.html',context)

#def infromations(request): 
    # get_params = []
    # get_params1 = []
    # get_params2 = []
    # get_params3 = []
    # get_params4 = []
    # get_params5 = []
    # for i in range(1, 8):
    #     get_params.append({'searchTotalKeyword': '자바','pageIndex': i})
    #     get_params1.append({'searchTotalKeyword': '클라우드','pageIndex': i})
    #     get_params2.append({'searchTotalKeyword': 'IOT','pageIndex': i})
    #     get_params3.append({'searchTotalKeyword': '빅데이터','pageIndex': i})
    #     get_params4.append({'searchTotalKeyword': '파이썬','pageIndex': i})
    #     get_params5.append({'searchTotalKeyword': 'AI','pageIndex': i})
    # responses = []
    # responses1 = []
    # responses2 = []
    # responses3 = []
    # responses4 = []
    # responses5 = []
    # for i in range(0, 7):
    #     responses.append(requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do",params=get_params[i]))
    #     responses1.append(requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do",params=get_params1[i]))
    #     responses2.append(requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do",params=get_params2[i]))
    #     responses3.append(requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do",params=get_params3[i]))
    #     responses4.append(requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do",params=get_params4[i]))        
    #     responses5.append(requests.post("http://hrd.go.kr/hrdp/co/pcoeo/PCOEO0101T.do",params=get_params5[i]))
    # htmls = []
    # htmls1 = []
    # htmls2 = []
    # htmls3 = []
    # htmls4 = []
    # htmls5 = []
    # for i in range(0,7):
    #     htmls.append(responses[i].text)
    #     htmls1.append(responses1[i].text)
    #     htmls2.append(responses2[i].text)
    #     htmls3.append(responses3[i].text)
    #     htmls4.append(responses4[i].text)
    #     htmls5.append(responses5[i].text)

    # soups = []
    # soups1 = []
    # soups2 = []
    # soups3 = []
    # soups4 = []
    # soups5 = []

    # for i in range(0,7):
    #     soups.append(BeautifulSoup(htmls[i],'html.parser'))
    #     soups1.append(BeautifulSoup(htmls1[i],'html.parser'))
    #     soups2.append(BeautifulSoup(htmls2[i],'html.parser'))
    #     soups3.append(BeautifulSoup(htmls3[i],'html.parser'))
    #     soups4.append(BeautifulSoup(htmls4[i],'html.parser'))
    #     soups5.append(BeautifulSoup(htmls5[i],'html.parser'))

    # title_lists = []
    # title_lists1 = []
    # title_lists2 = []
    # title_lists3 = []
    # title_lists4 = []
    # title_lists5 = []

    # for i in range(0,7):
    #     title_lists.append(soups[i].select('p[class=name]'))
    #     title_lists1.append(soups1[i].select('p[class=name]'))
    #     title_lists2.append(soups2[i].select('p[class=name]'))
    #     title_lists3.append(soups3[i].select('p[class=name]'))
    #     title_lists4.append(soups4[i].select('p[class=name]'))
    #     title_lists5.append(soups5[i].select('p[class=name]')) 
    # academy_lists = []
    # academy_lists1 = []
    # academy_lists2 = []
    # academy_lists3 = []
    # academy_lists4 = []
    # academy_lists5 = []
    # for i in range(0,7):
    #     academy_lists.append(soups[i].select('dl[class=academy]'))
    #     academy_lists1.append(soups1[i].select('dl[class=academy]'))
    #     academy_lists2.append(soups2[i].select('dl[class=academy]'))
    #     academy_lists3.append(soups3[i].select('dl[class=academy]'))
    #     academy_lists4.append(soups4[i].select('dl[class=academy]'))
    #     academy_lists5.append(soups5[i].select('dl[class=academy]'))
    # info_lists = []
    # info_lists1 = []
    # info_lists2 = []
    # info_lists3 = []
    # info_lists4 = []
    # info_lists5 = []

    # for i in range(0,7):
    #     info_lists.append(soups[i].select('ul[class=info]'))
    #     info_lists1.append(soups1[i].select('ul[class=info]'))
    #     info_lists2.append(soups2[i].select('ul[class=info]'))
    #     info_lists3.append(soups3[i].select('ul[class=info]'))
    #     info_lists4.append(soups4[i].select('ul[class=info]'))
    #     info_lists5.append(soups5[i].select('ul[class=info]'))

                 
    # code = 0 
    # # title list
    # for i in range(0,7):
    #     for tit in title_lists[i] :
    #         title = ''.join(tit.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, java_gugic_title = title).exists():
    #             information = Information()
    #             information.code = code
    #             information.java_gugic_title = title
    #             information.save()

    # for i in range(0,7):
    #     for tit in title_lists1[i] :
    #         title = ''.join(tit.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, cloud_gugic_title = title).exists():
    #             information = Information()
    #             information.code = code
    #             information.cloud_gugic_title = title
    #             information.save()

    # for i in range(0,7):
    #     for tit in title_lists2[i] :
    #         title = ''.join(tit.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, IOT_gugic_title = title).exists():
    #             information = Information()
    #             information.code = code
    #             information.IOT_gugic_title = title
    #             information.save()
    # for i in range(0,7):
    #     for tit in title_lists3[i] :
    #         title = ''.join(tit.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, BigData_gugic_title = title).exists():
    #             information = Information()
    #             information.code = code
    #             information.BigData_gugic_title = title
    #             information.save()
    # for i in range(0,7):
    #     for tit in title_lists4[i] :
    #         title = ''.join(tit.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, python_gugic_title = title).exists():
    #             information = Information()
    #             information.code = code
    #             information.python_gugic_title = title
    #             information.save()
    # for i in range(0,7):
    #     for tit in title_lists5[i] :
    #         title = ''.join(tit.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, AI_gugic_title = title).exists():
    #             information = Information()
    #             information.code = code
    #             information.AI_gugic_title = title
    #             information.save()



    # #academy
    # for i in range(0,7):
    #     for acd in academy_lists[i] :
    #         academy = ''.join(acd.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,java_gugic_academy = academy ).exists():
    #             information = Information()
    #             information.code = code
    #             information.java_gugic_academy = academy
    #             information.save()
    # for i in range(0,7):
    #     for acd in academy_lists1[i] :
    #         academy = ''.join(acd.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,cloud_gugic_academy = academy ).exists():
    #             information = Information()
    #             information.code = code
    #             information.cloud_gugic_academy = academy
    #             information.save()
    # for i in range(0,7):
    #     for acd in academy_lists2[i] :
    #         academy = ''.join(acd.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,IOT_gugic_academy = academy ).exists():
    #             information = Information()
    #             information.code = code
    #             information.IOT_gugic_academy = academy
    #             information.save()
    # for i in range(0,7):
    #     for acd in academy_lists3[i] :
    #         academy = ''.join(acd.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,BigData_gugic_academy = academy ).exists():
    #             information = Information()
    #             information.code = code
    #             information.BigData_gugic_academy = academy
    #             information.save()
    # for i in range(0,7):
    #     for acd in academy_lists4[i] :
    #         academy = ''.join(acd.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,python_gugic_academy = academy ).exists():
    #             information = Information()
    #             information.code = code
    #             information.python_gugic_academy = academy
    #             information.save()
    # for i in range(0,7):
    #     for acd in academy_lists5[i] :
    #         academy = ''.join(acd.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,AI_gugic_academy = academy ).exists():
    #             information = Information()
    #             information.code = code
    #             information.AI_gugic_academy = academy
    #             information.save()                                                            
    # #info
    # for i in range(0,7):
    #     for info in info_lists[i] :
    #         info = ''.join(info.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,java_gugic_info = info ).exists():
    #             information = Information()
    #             information.code = code
    #             information.java_gugic_info = info
    #             information.save()

    # for i in range(0,7):
    #     for info in info_lists1[i] :
    #         info = ''.join(info.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,cloud_gugic_info = info ).exists():
    #             information = Information()
    #             information.code = code
    #             information.cloud_gugic_info = info
    #             information.save()

    # for i in range(0,7):
    #     for info in info_lists2[i] :
    #         info = ''.join(info.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code, IOT_gugic_info = info ).exists():
    #             information = Information()
    #             information.code = code
    #             information.IOT_gugic_info = info
    #             information.save()

    # for i in range(0,7):
    #     for info in info_lists3[i] :
    #         info = ''.join(info.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,BigData_gugic_info = info ).exists():
    #             information = Information()
    #             information.code = code
    #             information.BigData_gugic_info = info
    #             information.save()
    # for i in range(0,7):
    #     for info in info_lists4[i] :
    #         info = ''.join(info.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,python_gugic_info = info ).exists():
    #             information = Information()
    #             information.code = code
    #             information.python_gugic_info = info
    #             information.save()
    # for i in range(0,7):
    #     for info in info_lists5[i] :
    #         info = ''.join(info.text.split())
    #         code = code + 1
    #         if not Information.objects.filter(code = code,AI_gugic_info = info ).exists():
    #             information = Information()
    #             information.code = code
    #             information.AI_gugic_info = info
    #             information.save()
    # informations = Information.objects.all()
    # context = {
    #     'informations': informations,
    # }
    # return render(request,'itess.html',context)
