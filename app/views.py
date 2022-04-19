from re import A
from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='FootBall')
    #webpages=Webpage.objects.filter(name__startswith='v')
    #webpages=Webpage.objects.filter(name__endswith='s')
    #webpages=Webpage.objects.filter(Q(name__startswith='d') & Q(url__startswith='https'))
    #webpages=Webpage.objects.filter(Q(topic_name__endswith='l') & Q(url__startswith='https'))
    #webpages=Webpage.objects.exclude(topic_name='FootBall')
    #webpages=Webpage.objects.all()[0:7:]
    #webpages=Webpage.objects.all()[-3]
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    d={'ws':webpages}
    return render(request,'display_webpages.html',d)

def display_access(request):
    access=AccessRecords.objects.all()
    #access=AccessRecords.objects.filter(date__day='03')
    #access=AccessRecords.objects.filter(date__month='03')
    #access=AccessRecords.objects.filter(date__year='2000')
    #access=AccessRecords.objects.filter(date__month__gt='03')
    access=AccessRecords.objects.filter(date__day__gte='03')

    



    d={'ac':access}
    return render(request,'display_access.html',d)