from django.shortcuts import render

def vol3(request):
    return render(request, 'web_view/IdolDreamingStation/vol3/index.html')

def index(request):
    return render(request, 'web_view/index.html')    