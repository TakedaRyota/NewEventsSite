from django.shortcuts import render

def index(request):
    return render(request, 'web_view/index.html')    

def idol_dreaming_station(request):
    return render(request, 'web_view/IdolDreamingStation/index.html')

def vol3(request):
    return render(request, 'web_view/IdolDreamingStation/vol3/index.html')
