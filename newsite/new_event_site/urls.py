from django.contrib import admin
from django.urls import path
from new_event_site.views import views

app_name = 'new_event_site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('IdolDreamingStation/', views.idol_dreaming_station),
    path('IdolDreamingStation/vol3/', views.vol3),
    path('20221124/', views.copy_dance_event),
    
    
]
