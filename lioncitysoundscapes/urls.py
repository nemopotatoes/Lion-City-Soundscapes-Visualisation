from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.about_page, name='about'),
    path('map/', views.map_page, name='map'),
    path('contact/', views.contact_page, name='contact'),
    path('recordings/', views.recordings_page, name='recordings')
]