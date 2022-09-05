from django.contrib import admin
from django.urls import path
from new_event_site.views import views

app_name = 'new_event_site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('artist/', views.artist),
    path('timetable/', views.timetable),
    path('ticket/', views.ticket),
    path('access/', views.access),
    path('guideline/', views.guideline),
]
