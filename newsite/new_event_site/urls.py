from django.contrib import admin
from django.urls import path
from new_event_site.views import views

app_name = 'new_event_site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('artist/', views.artist, name='artist'),
    path('timetable/', views.timetable, name='timetable'),
    path('ticket/', views.ticket, name='ticket'),
    path('access/', views.access, name='access'),
    path('guideline/', views.guideline, name='guideline'),
]
