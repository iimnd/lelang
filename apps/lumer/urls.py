
from apps.lumer.views import homePageView
from django.urls import path, include

urlpatterns = [
   
    path("", homePageView, name="homePageView"),
    
]