from django.contrib import admin
from django.urls import path
from new_event_site.views import views

app_name = 'new_event_site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('IdolDreamingStation/vol3/', views.vol3),
    path('', views.index),
]
