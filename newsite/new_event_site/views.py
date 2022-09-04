from django.shortcuts import render

def index(request):
    return render(request, 'web_view/index.html')

def about(request):
    return render(request, 'web_view/about/index.html')

def artist(request):
    return render(request, 'web_view/artist/index.html')

def timetable(request):
    return render(request, 'web_view/timetable/index.html')

def ticket(request):
    return render(request, 'web_view/ticket/index.html')

def access(request):
    return render(request, 'web_view/access/index.html')

def guideline(request):
    return render(request, 'web_view/guideline/index.html')
    