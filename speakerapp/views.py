from django.shortcuts import render
from .models import Speaker
# Create your views here.

def index(request):
    return render(request,"index.html")

def listSpeakers(request):
    speaker_lst = Speaker.objects.all()
    context = {'speaker_lst': speaker_lst}  
    return render(request, 'index.html', context=context)

def fetchSpeaker(request,speakerName):
    speakerDetail=Speaker.objects.get(name=speakerName)
    return render(request, 'details.html', {'spkr':speakerDetail})
