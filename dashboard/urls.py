from django.urls import path
from .views import home, about, help, tips

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('help/', help, name="help"),
    path('tips/', tips, name="tips"),
]