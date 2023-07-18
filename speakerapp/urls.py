from django.urls import path
from . import views

urlpatterns = [
    path('',views.listSpeakers,name='listSpeakers'),
    path('details/<str:speakerName>',views.fetchSpeaker,name='fetchSpeaker')
]
